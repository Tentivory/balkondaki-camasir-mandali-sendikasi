#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Balkondaki Çamaşır Mandalı Sendikası
Genel Kurul Simülatörü — sürüm 0.1-rüzgar

Bu yazılım, balkonun kuzeybatı köşesindeki mandalların
kollektif karar alma sürecini bilimsel ciddiyetle modellemektedir.
"""

from __future__ import annotations

import argparse
import base64
import random
import time
from dataclasses import dataclass

MANDALLAR = [
    "Ahmet Mandal (plastik, kırmızı)",
    "Ayşe Mandal (ahşap, kırık dişli)",
    "Kemal Mandal (paslanmaz, iddialı)",
    "Fatma Mandal (yayı gevşek, tecrübeli)",
    "Recep Mandal (ikiz mandal, tek oy)",
    "Sevgi Mandal (rengarenk, tarafsız görünüyor)",
    "Osman Mandal (ip üstünde kaymış)",
]

GUNDEM = [
    "Rüzgarın yönü değişti, çorapları tutuyor muyuz?",
    "Komşunun balkonuna kaçan çamaşır için diplomatik nota",
    "Güneş battı, mesai bitti mi yoksa neme karşı nöbet mi?",
    "Yeni gelen mandal sendikaya aidat ödeyecek mi?",
    "Kedi geçti, acil toplanma",
]

OYLAR = ["KABUL", "RET", "ÇEKİMSER", "RÜZGAR ALDI OYUMU"]


@dataclass
class Karar:
    madde: str
    sonuc: str
    katilim: int


def genel_kurul(tur: int = 3) -> list[Karar]:
    print("=" * 60)
    print("  BALKONDAKİ ÇAMAŞIR MANDALI SENDİKASI — GENEL KURUL")
    print("  Toplantı yeri: ipin en gerilimli noktası")
    print("=" * 60)
    kararlar: list[Karar] = []
    for i in range(tur):
        madde = random.choice(GUNDEM)
        print(f"\nGündem {i + 1}: {madde}")
        time.sleep(0.4)
        oylar = [random.choice(OYLAR) for _ in MANDALLAR]
        for uye, oy in zip(MANDALLAR, oylar):
            print(f"  - {uye}: {oy}")
        kabul = oylar.count("KABUL")
        ret = oylar.count("RET")
        if kabul > ret:
            sonuc = "KABUL EDİLDİ (çamaşır duruyor)"
        elif ret > kabul:
            sonuc = "REDDEDİLDİ (çamaşır uçtu, tutanak tutulacak)"
        else:
            sonuc = "BERABERE — rüzgar başkanlık etti"
        print(f"Karar: {sonuc}")
        kararlar.append(Karar(madde, sonuc, len(MANDALLAR)))
    return kararlar


def gizli_arsiv() -> None:
    # Bu fonksiyon sadece --arsiv ile açılır. Merak etme, balkon sessiz.
    paket = b"aWt0aWRhciBkYSBhc2xpbmRhIGJpciBtYW5kYWxkaXI6IHNpa2kgdHV0YXIsIHJ1emdhciBnZWxpbmNlIHNlcyBjaWthcmlyLiBoZXIgc2VuemV0IGt1cnVtdSBrZW5kaSBpcGluZSBhc2FyLiAtIGFyşiv notu"
    try:
        print(base64.b64decode(paket).decode("utf-8", errors="replace"))
    except Exception:
        print("(arşiv nemden bozulmuş)")


def damga() -> None:
    print("\n" + "-" * 60)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok — Tentivory")
    print("26 Eylül 2026, Cumartesi, saat yaklaşık 10:02 +03")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (ciddi)")
    print("Mandal sendikası mührü: *klik* (ciddi değil)")
    print("-" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(description="Mandal sendikası genel kurul simülatörü")
    parser.add_argument("--tur", type=int, default=3, help="gündem maddesi sayısı")
    parser.add_argument("--arsiv", action="store_true", help="nemli arşivi aç")
    args = parser.parse_args()
    genel_kurul(max(1, args.tur))
    if args.arsiv:
        print("\n[ARŞİV]")
        gizli_arsiv()
    damga()


if __name__ == "__main__":
    main()
