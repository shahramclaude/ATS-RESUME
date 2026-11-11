# -*- coding: utf-8 -*-
"""style_guard.py — håndhæver den bindende policy "VARIERET SPROG, STIL OG KULTURTILPASNING"
(master/README.md, bruger 04.11.2026) maskinelt, så stilvariationen ikke afhænger af hukommelse.

Læser logtabellen i master/STILREGISTER.md og kontrollerer det planlagte byg mod de seneste
dokumenter:

  * Åbningsgreb: samme greb må ikke bruges to gange i træk (hård fejl), og et greb brugt inden
    for de sidste to dokumenter giver advarsel.
  * Register: samme register som det seneste dokument er en hård fejl; gentagelse inden for de
    sidste tre giver advarsel (kun i orden med et markant andet udtryk inden for registret).
  * Struktur: samme side-1-struktur som sidste dokument er en hård fejl; gentagelse inden for de
    sidste fire giver advarsel.
  * Variationskravet: mindst TO af de tre (åbningsgreb, struktur, register) skal skifte i forhold
    til det seneste dokument. Er kun ét skiftet, fejler kontrollen.

Brug:
    python3 scripts/style_guard.py --register "Ingeniør-præcis" --opening F --structure "Kunderejsen"
    python3 scripts/style_guard.py --list           # vis hvad der er brugt
"""
import argparse
import re
import sys

LOG = 'master/STILREGISTER.md'
MIN_CHANGES = 2
OPENING_BLOCK_WINDOW = 2
REGISTER_BLOCK_WINDOW = 3
STRUCTURE_BLOCK_WINDOW = 4


def load_rows(path=LOG):
    """Returnerer logrækker som dicts, ældste først."""
    rows = []
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            if not line.startswith('| #'):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 6:
                continue
            pr, company, register, opening, structure = cells[0], cells[1], cells[2], cells[3], cells[4]
            letter = ''
            m = re.match(r'([A-K])\b', opening)
            if m:
                letter = m.group(1)
            rows.append({
                'pr': pr,
                'company': company,
                'register': register,
                'register_key': register.split('/')[0].strip().lower(),
                'opening': opening,
                'opening_key': letter,
                'structure': structure,
                'structure_key': structure.split('(')[0].strip().lower(),
            })
    return rows


def _window(rows, n):
    return rows[-n:] if len(rows) >= n else rows


def check(rows, register, opening, structure):
    """Returnerer (fejl, advarsler, skift) som lister."""
    errors, warnings = [], []
    reg_key = register.split('/')[0].strip().lower()
    str_key = structure.split('(')[0].strip().lower()
    op_key = opening.strip().upper()[:1]

    last = rows[-1] if rows else None
    changes = 0
    if last:
        if op_key != last['opening_key']:
            changes += 1
        if reg_key != last['register_key']:
            changes += 1
        if str_key != last['structure_key']:
            changes += 1

    # åbningsgreb
    recent_openings = [r['opening_key'] for r in _window(rows, OPENING_BLOCK_WINDOW)]
    if recent_openings and op_key == recent_openings[-1]:
        errors.append(f"åbningsgreb {op_key} blev brugt i det seneste dokument ({rows[-1]['pr']}) — "
                      f"vælg et andet greb")
    elif op_key in recent_openings:
        warnings.append(f"åbningsgreb {op_key} er brugt inden for de sidste {OPENING_BLOCK_WINDOW} "
                        f"dokumenter — kun i orden hvis grebet udfoldes markant anderledes")

    # register
    recent = _window(rows, REGISTER_BLOCK_WINDOW)
    same = [r['pr'] for r in recent if r['register_key'] == reg_key]
    if last and reg_key == last['register_key']:
        errors.append(f"register '{register}' blev brugt i det seneste dokument ({last['pr']}) — "
                      f"vælg et andet register eller skift udtrykket markant inden for det")
    elif same:
        warnings.append(f"register '{register}' er også brugt i {', '.join(same)} — i orden hvis "
                        f"ordvalg, sætningsrytme og sektionsoverskrifter er tydeligt anderledes")

    # struktur
    recent_structures = [r['structure_key'] for r in _window(rows, STRUCTURE_BLOCK_WINDOW)]
    if recent_structures and str_key == recent_structures[-1]:
        errors.append(f"strukturen '{structure}' blev brugt i det seneste dokument ({rows[-1]['pr']}) — "
                      f"vælg en anden struktur")
    elif str_key in recent_structures:
        warnings.append(f"strukturen '{structure}' er brugt inden for de sidste {STRUCTURE_BLOCK_WINDOW} "
                        f"dokumenter — kun i orden med en klar ny vinkel")

    if last and changes < MIN_CHANGES:
        errors.append(f"kun {changes} af tre (åbningsgreb, struktur, register) skifter i forhold til "
                      f"{last['pr']} — policyen kræver mindst {MIN_CHANGES}")

    return errors, warnings, changes


def main():
    ap = argparse.ArgumentParser(description='Kontrollerer stilvariation mod master/STILREGISTER.md.')
    ap.add_argument('--register', help='planlagt register, fx "Ingeniør-præcis"')
    ap.add_argument('--opening', help='planlagt åbningsgreb, bogstav A-J eller navnet')
    ap.add_argument('--structure', help='planlagt side-1-struktur, fx "Kunderejsen"')
    ap.add_argument('--list', action='store_true', help='vis de seneste dokumenters stilvalg')
    ap.add_argument('--log', default=LOG, help='sti til stilregisteret')
    args = ap.parse_args()

    rows = load_rows(args.log)

    if args.list or not (args.register and args.opening and args.structure):
        print(f"STILREGISTER : {len(rows)} dokumenter logget")
        for r in rows[-6:]:
            print(f"  {r['pr']:<6} {r['register']:<28} åbning {r['opening_key']:<2} {r['structure'][:52]}")
        if not args.list:
            print("\nBrug --register --opening --structure for at kontrollere det næste byg.")
        return 0

    errors, warnings, changes = check(rows, args.register, args.opening, args.structure)

    print(f"REGISTER     : {args.register}")
    print(f"ÅBNINGSGREB  : {args.opening}")
    print(f"STRUKTUR     : {args.structure}")
    print(f"SKIFT        : {changes}/3 i forhold til {rows[-1]['pr'] if rows else '—'}")
    print()
    for w in warnings:
        print(f"  ⚠ {w}")
    for e in errors:
        print(f"  ✗ {e}")
    if errors:
        print("\n✗ Stilvariationen er ikke i orden — vælg om, før der bygges.")
        return 1
    print("✓ Stilvariation ok: åbning, struktur og register er tilstrækkeligt nye.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
