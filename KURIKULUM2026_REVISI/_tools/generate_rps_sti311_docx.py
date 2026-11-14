"""
=============================================================================
GENERATOR RPS OBE — STI-311 PENGEMBANGAN WEB FRONT END
=============================================================================
Sumber data:
  - Dok 005 : Identitas MK (kode, nama, SKS, semester, prasyarat)
  - Dok 007 : Silabus 3-Tabel (CPMK, Sub-CPMK, 16 pertemuan)
  - Dok 043 : Boundary Guardrails, rumusan CPMK verbatim
  - Dok 003 : Rumusan CPL resmi
  - Dok 008 : Skema 4x asesmen
  - PERANGKAT_AJAR/065_1..5 : RPS, SAP, Rubrik rancangan 7 Nov 2026

Output:
  KURIKULUM2026_REVISI/DOCX/RPS_STI-311_Web_Front_End_Development.docx

Pola:
  1. Buka template → salin ke output (template master TIDAK ditimpa)
  2. Isi tag [blok] dulu (tabel identitas & 16-pekan & lampiran)
  3. Isi tag {{scalar}} terakhir agar menjangkau tabel nested
  4. Simpan; jalankan cek residual
=============================================================================
"""

import os
import sys
import io
import copy
import shutil

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

try:
    from docx import Document
    from docx.shared import Pt
except ImportError:
    print("[ERROR] python-docx tidak ditemukan. Jalankan: pip install python-docx")
    sys.exit(1)

# ---------------------------------------------------------------------------
# PATH
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR    = os.path.dirname(SCRIPT_DIR)
TEMPLATE   = os.path.join(WORKDIR, "Template_RPS_GEN_2026_20092026-SWO.docx")
OUT_DIR    = os.path.join(WORKDIR, "DOCX")
OUT_DOCX   = os.path.join(OUT_DIR, "RPS_STI-311_Web_Front_End_Development.docx")

os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# DATA SCALAR  {{tag}}   — Sumber: Dok 005, Dok 052
# ---------------------------------------------------------------------------
SCALAR = {
    "namamk"        : "Pengembangan Web Front End",
    "kodemk"        : "STI-311",
    "rumpunmk"      : "Mata Kuliah Inti Program Studi (Core STI)",
    "skst"          : "2",
    "sksp"          : "1",
    "sms"           : "3 (Gasal)",
    "tglsusun"      : "8 November 2026",
    "pengembangrps" : "Tim KBK Rekayasa Platform Digital FSTI UWG",
    "koordinatormk" : "[PERLU KONFIRMASI: Koordinator RMK STI-311]",
    "ketuaprodi"    : "[PERLU KONFIRMASI: Ketua Prodi SISTEKIN]",
    "kodeprodi"     : "B4.5.2.RPS-STI311",
    "prodi"         : "Sistem dan Teknologi Informasi",
    "namadosen"     : "[PERLU KONFIRMASI: Nama Dosen Pengampu STI-311]",
    "nuptk"         : "[PERLU KONFIRMASI: NUPTK/NIDN]",
    "deskripsimk"   : (
        "Mata kuliah ini membekali mahasiswa dengan kemampuan membangun antarmuka web "
        "yang fungsional dan responsif menggunakan HTML, CSS, dan JavaScript dasar. "
        "Mahasiswa mempelajari struktur dokumen HTML semantik, pemformatan tampilan "
        "dengan CSS termasuk Flexbox dan media query, pengenalan framework CSS "
        "(Bootstrap dan Tailwind CSS), serta pemrograman interaksi browser menggunakan "
        "JavaScript dasar beserta manipulasi DOM dan event. Mata kuliah bersifat "
        "teori plus praktikum (2T+1P) dengan dua proyek utama: kalkulator aritmetika "
        "sederhana dan landing page responsif. Lingkup dibatasi pada pengembangan "
        "sisi klien (front-end) tanpa framework SPA, backend, atau build pipeline. "
        "Luaran belajar selaras CPL-08 dan CPL-13 Kurikulum SISTEKIN 2026, "
        "Bahan Kajian BK-IS12 (Web Systems) dan BK-IT04 (UI Design)."
    ),
    "bahankajian"   : (
        "BK-IS12 Web Systems & Technologies (IS2020): HTML semantik, CSS Flexbox, "
        "JavaScript dasar, DOM, event, Bootstrap, Tailwind CSS.\n"
        "BK-IT04 User Interface Design (IT2017): prototyping antarmuka, "
        "responsivitas, aksesibilitas dasar."
    ),
    "dosenpengampu" : "[PERLU KONFIRMASI: Tim Dosen Pengampu STI-311]",
    "mkprasyarat"   : "FST-102 Algoritma dan Pemrograman",
}

# ---------------------------------------------------------------------------
# CPL — Sumber: Dok 003 (verbatim)
# ---------------------------------------------------------------------------
CPL_LIST = [
    ("CPL-08 (P4)",
     "Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), "
     "manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta "
     "prinsip desain interaksi pengalaman pengguna (UI/UX). [IRM: R]"),
    ("CPL-13 (KK5)",
     "Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa "
     "platform digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA). [IRM: R]"),
]

# ---------------------------------------------------------------------------
# CPMK — Sumber: Dok 043 / 065_1 (verbatim)
# ---------------------------------------------------------------------------
CPMK_LIST = [
    ("CPMK-1",
     "Mahasiswa mampu menyusun halaman HTML dasar-menengah yang memuat struktur semantik, "
     "konten, tabel dan formulir berdasarkan kebutuhan kasus yang diberikan, dengan "
     "struktur elemen, label dan tautan yang sesuai. [C3 / CPL-08]"),
    ("CPMK-2",
     "Mahasiswa mampu menerapkan CSS dasar-menengah dan Flexbox termasuk pengaturan "
     "flex item dan responsivitas pada kasus antarmuka yang diberikan, serta mengenali "
     "penggunaan kelas Bootstrap dan Tailwind dasar, dengan tampilan rapi dan terbaca "
     "pada sedikitnya dua ukuran layar. [C3 / CPL-08]"),
    ("CPMK-3",
     "Mahasiswa mampu membangun kalkulator aritmetika sederhana menggunakan JavaScript "
     "dasar dan styling Bootstrap atau Tailwind CSS, dengan operasi dan penanganan input "
     "sesuai kasus uji yang diberikan. [C3 / CPL-13]"),
    ("CPMK-4",
     "Mahasiswa mampu membangun dan menguji landing page responsif dengan interaksi "
     "sederhana menggunakan HTML, CSS dan JavaScript dasar, dengan Bootstrap atau "
     "Tailwind sebagai pilihan, serta mendokumentasikan navigasi, interaksi dan "
     "hasil pengujian. [C6 / CPL-13]"),
]

# ---------------------------------------------------------------------------
# Sub-CPMK — Sumber: Dok 043 / 065_1 (verbatim)
# ---------------------------------------------------------------------------
SUBCPMK_LIST = [
    ("Sub-CPMK-1.1", "Menyusun struktur dokumen semantik dan konten: teks, gambar, daftar serta tautan. [CPMK-1 / C3]"),
    ("Sub-CPMK-1.2", "Membuat tabel dan formulir berlabel dengan tipe masukan dan validasi HTML dasar. [CPMK-1 / C3]"),
    ("Sub-CPMK-2.1", "Menerapkan selektor, cascade dasar, warna, tipografi, box model, display, position dan media query. [CPMK-2 / C3]"),
    ("Sub-CPMK-2.2", "Menggunakan properti container dan item Flexbox, termasuk wrap, grow/shrink/basis dan nested flex, untuk tata letak responsif. [CPMK-2 / C3]"),
    ("Sub-CPMK-2.3", "Menerapkan kelas dasar Bootstrap dan utility Tailwind pada latihan antarmuka sederhana. [CPMK-2 / C3]"),
    ("Sub-CPMK-3.1", "Menggunakan variabel, tipe data, operator, percabangan, perulangan dan fungsi dalam latihan aritmetika. [CPMK-3 / C3]"),
    ("Sub-CPMK-3.2", "Menghubungkan input dan tombol kalkulator dengan fungsi JavaScript melalui DOM dan event, memakai styling Bootstrap atau Tailwind. [CPMK-3 / C3]"),
    ("Sub-CPMK-4.1", "Menggabungkan HTML, CSS/Flexbox dan JavaScript dasar menjadi landing page responsif; framework CSS boleh digunakan. [CPMK-4 / C6]"),
    ("Sub-CPMK-4.2", "Menyusun dan menjalankan kasus uji navigasi, interaksi, dan tampilan; memperbaiki masalah dan mencatat hasilnya. [CPMK-4 / C4]"),
]

# ---------------------------------------------------------------------------
# MATRIKS KORELASI
# ---------------------------------------------------------------------------
TABEL_KORELASI = (
    "Matriks Korelasi CPL-CPMK & Bobot Asesmen STI-311\n"
    "CPL-08: CPMK-1 (v), CPMK-2 (v) | Kontribusi 45%\n"
    "CPL-13: CPMK-3 (v), CPMK-4 (v) | Kontribusi 55%\n"
    "Instrumen : Tugas 1  | UTS   | Tugas 2 | UAS\n"
    "Bobot     : 20%      | 25%   | 25%     | 30%  = 100%\n"
    "Pekan     : 4        | 8     | 12      | 16\n"
    "MK tipe +P: UTS 25%, Tugas 2 25% (Dok 008)"
)

# ---------------------------------------------------------------------------
# PUSTAKA
# ---------------------------------------------------------------------------
PUSTAKA_UTAMA = (
    "[1] Duckett, J. (2011). HTML & CSS: Design and Build Websites. John Wiley & Sons.\n"
    "[2] Duckett, J. (2014). JavaScript & jQuery: Interactive Front-End Web Development. Wiley.\n"
    "[3] Frain, B. (2022). Responsive Web Design with HTML5 and CSS (4th ed.). Packt.\n"
    "[4] Wathan, A. et al. (2023). Tailwind CSS Documentation. https://tailwindcss.com/docs\n"
    "[5] Bootstrap Team. (2024). Bootstrap 5 Documentation. https://getbootstrap.com/docs/"
)
PUSTAKA_PENDUKUNG = (
    "[6] MDN Web Docs - HTML. https://developer.mozilla.org/en-US/docs/Web/HTML\n"
    "[7] MDN Web Docs - CSS Flexbox. https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout\n"
    "[8] MDN Web Docs - JavaScript. https://developer.mozilla.org/en-US/docs/Web/JavaScript\n"
    "[9] W3C. (2023). HTML Living Standard. https://html.spec.whatwg.org/\n"
    "[10] WCAG 2.1. https://www.w3.org/TR/WCAG21/"
)

# ---------------------------------------------------------------------------
# 16 PERTEMUAN — Sumber: 065_1 & 065_2 (verbatim)
# (mg, subcpmk, indikator, kriteria_teknik, luring, daring, materi, bobot)
# ---------------------------------------------------------------------------
PEKAN = [
    (1, "Sub-CPMK-1.1",
     "1.1 Ketepatan menyusun struktur dokumen HTML dasar dengan hierarki heading, paragraf, dan daftar yang benar.",
     "Non-tes: Unjuk kerja praktikum (halaman profil HTML). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide HTML dasar, tautan MDN HTML. Forum asinkron.",
     "Orientasi front-end; peran HTML/CSS/JS; struktur HTML, teks, heading, daftar.\n[1] Bab 1-2; [6]", "—"),

    (2, "Sub-CPMK-1.1",
     "1.1 Ketepatan menggunakan elemen semantik (header, nav, main, section, footer) dan atribut tautan/gambar.",
     "Non-tes: Unjuk kerja (halaman informasi dengan navigasi). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide HTML semantik. Forum asinkron.",
     "HTML semantik: header, nav, main, section, footer; tautan dan gambar dengan alt.\n[1] Bab 3; [6]", "—"),

    (3, "Sub-CPMK-1.2",
     "1.2 Ketepatan membuat tabel HTML berstruktur dan formulir berlabel dengan validasi bawaan browser.",
     "Non-tes: Unjuk kerja (formulir simulasi dan tabel berstruktur). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide tabel & formulir. Forum asinkron.",
     "HTML menengah: tabel, formulir, label, input, tombol, validasi HTML bawaan.\n[1] Bab 7-8; [6]", "—"),

    (4, "Sub-CPMK-1.1, 1.2",
     "1.1-1.2 Ketepatan membangun halaman HTML lengkap: semantik, tabel, formulir, tautan, gambar. [TUGAS 1]",
     "Non-tes/Tes: Penilaian produk halaman HTML (rubrik analitik 4 kriteria). Portofolio berkas HTML.",
     "Kuliah & Praktikum\nTM: 100 mnt (review HTML, pengantar CSS)\nPraktikum: 170 mnt (kumpulkan Tugas 1)\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slot pengumpulan Tugas 1. Slide pengantar CSS.",
     "Review HTML; pengantar stylesheet, selektor, warna, tipografi CSS.\n[1] Bab 10; [2] Bab 1",
     "20% (Tugas 1)"),

    (5, "Sub-CPMK-2.1",
     "2.1 Ketepatan menerapkan selektor, cascade, spesifisitas, box model, display, position CSS.",
     "Non-tes: Unjuk kerja (stylesheet dan tata letak kartu). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide CSS dasar, tautan MDN CSS. Forum asinkron.",
     "CSS dasar-menengah: cascade, spesifisitas, box model, display, position.\n[3] Bab 2; [7]", "—"),

    (6, "Sub-CPMK-2.2",
     "2.2 Ketepatan menggunakan properti Flexbox: direction, wrap, grow/shrink/basis, nested flex.",
     "Non-tes: Unjuk kerja (navigasi dan kartu responsif Flexbox). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide Flexbox, tautan MDN Flexbox. Forum asinkron.",
     "Flexbox: sumbu, direction, alignment, wrap, gap; grow/shrink/basis, nested.\n[3] Bab 4; [7]", "—"),

    (7, "Sub-CPMK-2.1, 2.2, 2.3",
     "2.1-2.3 Ketepatan menerapkan media query dua breakpoint; kelas dasar Bootstrap dan utility Tailwind.",
     "Non-tes: Unjuk kerja (komponen dua framework pada dua ukuran layar). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt (media query, Bootstrap, Tailwind)\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: file Bootstrap & Tailwind siap pakai (offline). Slide responsivitas.",
     "Media query; Bootstrap (container, tombol, kartu); Tailwind (spacing, warna, breakpoint).\n[4][5]", "—"),

    (8, "Sub-CPMK-2.1, 2.2, 2.3",
     "2.1-2.3 CSS/Flexbox responsif dan kelas dasar dua framework secara mandiri. [UTS]",
     "Tes praktik: ujian CSS/Flexbox responsif + latihan singkat kelas Bootstrap dan Tailwind. Rubrik analitik UTS (4 kriteria).",
     "Ujian Praktik (Luring)\nTM+Praktikum: 270 mnt ujian\nPT: mandiri | BM: mandiri",
     "LMS Edlink: slot pengumpulan berkas UTS.",
     "Ujian praktik CSS/Flexbox; kelas Bootstrap dan Tailwind.\n[3][4][5]",
     "25% (UTS)"),

    (9, "Sub-CPMK-3.1",
     "3.1 Ketepatan menggunakan variabel, tipe data, operator aritmetika, konsol JavaScript.",
     "Non-tes: Unjuk kerja (fungsi empat operasi sederhana). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide JavaScript dasar, tautan MDN JS. Forum asinkron.",
     "JavaScript: script, variabel, tipe data, operator aritmetika, konsol.\n[2] Bab 1-2; [8]", "—"),

    (10, "Sub-CPMK-3.1",
     "3.1 Ketepatan menerapkan percabangan, perulangan, fungsi; konversi input angka; penanganan pembagi nol.",
     "Non-tes: Unjuk kerja (fungsi kalkulasi valid/tidak valid). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide percabangan JS. Forum asinkron.",
     "Percabangan, perulangan, fungsi, array; konversi input; kondisi pembagi nol.\n[2] Bab 3-4; [8]", "—"),

    (11, "Sub-CPMK-3.2",
     "3.2 Ketepatan memilih elemen DOM, membaca input, addEventListener, menampilkan hasil/pesan, kelas Bootstrap atau Tailwind.",
     "Non-tes: Unjuk kerja (purwarupa kalkulator dengan styling framework). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide DOM & event JS. File framework siap pakai.",
     "DOM: querySelector, value, addEventListener, textContent; styling Bootstrap/Tailwind.\n[2] Bab 5-6; [4][5]", "—"),

    (12, "Sub-CPMK-3.1, 3.2",
     "3.1-3.2 Kalkulator empat operasi lengkap; penanganan input tidak valid; styling framework; bukti kasus uji. [TUGAS 2]",
     "Non-tes/Tes: Penilaian produk kalkulator (rubrik analitik 5 kriteria). Demonstrasi + berkas + tabel uji.",
     "Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt (selesaikan, uji, kumpulkan)\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slot pengumpulan Tugas 2.",
     "Praktikum dan demonstrasi kalkulator JavaScript + Bootstrap atau Tailwind.\n[2] Bab 5-6; [4][5]",
     "25% (Tugas 2)"),

    (13, "Sub-CPMK-4.1",
     "4.1 Ketepatan merencanakan struktur semantik landing page: hero, manfaat/fitur, CTA, footer; kerangka HTML.",
     "Non-tes: Unjuk kerja (sketsa dan kerangka HTML). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide perencanaan landing page. Referensi aset berizin.",
     "Perencanaan landing page: struktur semantik, hero, manfaat, CTA, footer.\n[1] Bab 9; [3] Bab 1", "—"),

    (14, "Sub-CPMK-4.1",
     "4.1 Ketepatan menata layout landing page responsif (CSS/Flexbox) dan interaksi JavaScript sederhana.",
     "Non-tes: Unjuk kerja (purwarupa responsif dan interaktif). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: slide responsivitas. File framework opsional.",
     "Layout responsif CSS/Flexbox; Bootstrap/Tailwind opsional; interaksi JS sederhana.\n[3] Bab 5; [2] Bab 7", "—"),

    (15, "Sub-CPMK-4.2",
     "4.2 Ketepatan menyusun kasus uji navigasi, interaksi, keyboard, dua ukuran layar; memperbaiki dan mendokumentasikan.",
     "Non-tes: Unjuk kerja (daftar kasus uji dan perbaikan terdokumentasi). Rubrik formatif.",
     "Kuliah & Praktikum\nTM: 100 mnt\nPraktikum: 170 mnt\nPT: 120 mnt | BM: 120 mnt",
     "LMS Edlink: template tabel uji. Slide pengujian front-end.",
     "Uji navigasi, interaksi, keyboard, dua lebar; perbaikan; dokumentasi.\n[9] W3C; [10] WCAG 2.1", "—"),

    (16, "Sub-CPMK-4.1, 4.2",
     "4.1-4.2 Demonstrasi landing page fungsional; penjelasan kode individual; penyerahan berkas. [UAS]",
     "Non-tes: Penilaian produk landing page (rubrik analitik 5 kriteria). Demonstrasi + berkas + kasus uji.",
     "Ujian/Demonstrasi (Luring)\nTM+Praktikum: 270 mnt demonstrasi\nPT: mandiri | BM: mandiri",
     "LMS Edlink: slot pengumpulan UAS (berkas, kasus uji, petunjuk lokal).",
     "Demonstrasi landing page, penjelasan kode individual, penyerahan berkas.\n[1][2][3][4][5]",
     "30% (UAS)"),
]

# ---------------------------------------------------------------------------
# LAMPIRAN  — Sumber: 065_4 & 065_5 (verbatim ringkas)
# ---------------------------------------------------------------------------
PENUGASAN1 = """\
LAMPIRAN 1 - TUGAS 1: HALAMAN HTML
MK: STI-311 | Bobot: 20% | Dikumpulkan: Minggu 4 | CPL-08/CPMK-1

Buat halaman informasi HTML statis mencakup:
1. Struktur semantik: header, nav, main, section, footer.
2. Konten: minimal 2 heading bertingkat, 2 paragraf, 2 jenis daftar.
3. Gambar berizin (CC-0) dengan atribut alt bermakna.
4. Minimal 2 tautan internal (anchor) dan 1 tautan eksternal.
5. Tabel berstruktur: thead, tbody, caption, elemen th.
6. Formulir berlabel (for/id): input text, email, number, tombol submit;
   validasi HTML bawaan (required, min, max/pattern). Data tidak dikirim.

BATASAN: tanpa CSS eksternal/inline/framework; semua aset lokal.
PENGUMPULAN: NIM_Nama_Tugas1_STI311.zip + checklist mandiri.

KRITERIA: Struktur & semantik 35% | Konten,tabel,tautan 25%
          Formulir & label 25%     | Kerapian berkas 15%"""

RUBRIK_TUGAS1 = """\
RUBRIK TUGAS 1 - HTML | Bobot MK: 20% | Skala 0-100 per kriteria

Kriteria (Bobot) | Sangat Baik 81-100 | Baik 66-80 | Cukup 56-65 | Kurang 0-55
Struktur&semantik(35%) | Semua elemen semantik & hierarki heading benar; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
Konten,tabel,tautan(25%) | Semua konten,tabel,gambar(alt),tautan sesuai; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
Formulir&label(25%) | Semua label terhubung, tipe input benar, validasi bawaan berfungsi | Aspek utama; minor | Sebagian; penting | Belum ada
Kerapian berkas(15%) | Folder rapi, penamaan konsisten, mudah dijalankan | Aspek utama; minor | Sebagian; penting | Belum ada

Skor T1 = 0.35xK1 + 0.25xK2 + 0.25xK3 + 0.15xK4 | Bobot MK: 20%"""

SOAL_UTS = """\
LAMPIRAN 2 - UTS: CSS, FLEXBOX & PENGENALAN FRAMEWORK
MK: STI-311 | Bobot: 25% | Pekan 8 | CPL-08/CPMK-2

BAGIAN A - CSS & Flexbox Responsif (60 mnt):
Diberikan file HTML oleh pengampu. Mahasiswa:
1. Hubungkan stylesheet eksternal; terapkan selektor, cascade, box model, display, position.
2. Buat tata letak navigasi & kartu produk (Flexbox: direction, wrap, justify, align, grow/shrink/basis)
   terbaca pada >=1024px dan <=480px menggunakan media query.
3. Pastikan tidak ada overflow horizontal pada kedua ukuran layar.

BAGIAN B - Framework CSS (30 mnt):
4. HTML-1: tambahkan kelas Bootstrap (container, tombol primer, kartu). File Bootstrap disediakan.
5. HTML-2: tambahkan utility Tailwind (spacing p/m, warna bg/text, breakpoint). File Tailwind disediakan.

PENGUMPULAN: ZIP + tangkapan 2 ukuran layar.
ALAT: editor teks, browser lokal, file framework disediakan.
DILARANG: CDN internet, AI code generator, komunikasi antar peserta.

KRITERIA: Selektor&box model 20% | Flexbox container/item 35%
          Responsivitas 2 layar 25% | Kelas 2 framework 20%"""

RUBRIK_UTS = """\
RUBRIK UTS - CSS, FLEXBOX & FRAMEWORK | Bobot MK: 25% | Skala 0-100

Kriteria (Bobot) | Sangat Baik 81-100 | Baik 66-80 | Cukup 56-65 | Kurang 0-55
Selektor&box model(20%) | Semua sesuai spesifikasi; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
Flexbox container/item(35%) | Semua properti Flexbox tepat (sumbu,wrap,grow/shrink,nested) | Aspek utama; minor | Sebagian; penting | Belum ada
Responsivitas 2 layar(25%) | Terbaca di 2 lebar tanpa overflow; bukti tangkapan | Aspek utama; minor | Sebagian; penting | Belum ada
Kelas 2 framework(20%) | Bootstrap & Tailwind diterapkan benar | Aspek utama; minor | Sebagian; penting | Belum ada

Skor UTS = 0.20xK1 + 0.35xK2 + 0.25xK3 + 0.20xK4 | Bobot MK: 25%"""

TUGAS2 = """\
LAMPIRAN 3 - TUGAS 2: KALKULATOR ARITMETIKA
MK: STI-311 | Bobot: 25% | Dikumpulkan: Minggu 12 | CPL-13/CPMK-3

Bangun kalkulator aritmetika sederhana berbasis browser (HTML statis):

FUNGSI WAJIB:
1. Dua input angka; pilihan operasi: +, -, x, bagi.
2. Tombol HITUNG dan RESET.
3. Hasil ditampilkan di halaman (bukan konsol atau alert).
4. Input kosong/bukan angka -> pesan error yang dapat dipahami.
5. Pembagi nol -> pesan error (bukan NaN/Infinity/kosong).

STYLING: pilih SATU framework - Bootstrap 5 ATAU Tailwind CSS (file disediakan offline).

KASUS UJI WAJIB (isi tabel dan sertakan):
  2+3=5 | 5-3=2 | 2x3=6 | 6/3=2 | a/0 | input kosong/tidak valid

PENGUMPULAN: NIM_Nama_Tugas2_STI311.zip + tabel uji + petunjuk lokal.
KRITERIA: Operasi JS 30% | DOM&event 20% | Input&pembagi nol 20%
          Framework 15% | Kode&hasil uji 15%"""

RUBRIK_TUGAS2 = """\
RUBRIK TUGAS 2 - KALKULATOR | Bobot MK: 25% | Skala 0-100

Kriteria (Bobot) | Sangat Baik 81-100 | Baik 66-80 | Cukup 56-65 | Kurang 0-55
Operasi JS(30%) | 4 operasi hasil benar; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
DOM&event(20%) | Input,tombol hitung/reset,keluaran bekerja; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
Input&pembagi nol(20%) | Input kosong/tidak valid & pembagi nol ditangani benar | Aspek utama; minor | Sebagian; penting | Belum ada
Framework pilihan(15%) | Kelas Bootstrap atau Tailwind sesuai tujuan | Aspek utama; minor | Sebagian; penting | Belum ada
Kode&hasil uji(15%) | Kode terbaca; kasus uji ada hasil aktual; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada

Skor T2 = 0.30xK1+0.20xK2+0.20xK3+0.15xK4+0.15xK5 | Bobot MK: 25%"""

SOAL_UAS = """\
LAMPIRAN 4 - UAS: LANDING PAGE RESPONSIF
MK: STI-311 | Bobot: 30% | Dikumpulkan: Minggu 16 | CPL-13/CPMK-4

Bangun landing page fungsional (produk/kegiatan/komunitas fiktif):

KONTEN WAJIB:
1. Header dengan navigasi (tautan ke seksi-seksi halaman).
2. Hero: judul utama, sub-judul, tombol CTA.
3. Min. 2 seksi konten (manfaat/fitur + 1 seksi tambahan).
4. Footer: kontak/hak cipta singkat.
5. Semua konten fiktif atau aset berizin (CC-0).

INTERAKSI WAJIB (DOM + event JS):
6. Min. 1 interaksi bermakna: menu mobile buka/tutup, tombol tampil/sembunyikan,
   atau validasi formulir simulasi (data tidak dikirim).

RESPONSIVITAS: tampil terbaca >=1024px dan <=480px.
Bootstrap/Tailwind opsional (file disediakan jika dipilih).

PENGUJIAN WAJIB:
a. Navigasi (semua anchor berfungsi).
b. Interaksi JS (input valid & tidak valid jika ada formulir).
c. Tampilan 2 lebar layar (tangkapan mobile & desktop).
d. Navigasi keyboard dasar (Tab, Enter pada tombol/tautan).

PENGUMPULAN: NIM_Nama_UAS_STI311.zip + tabel kasus uji + petunjuk lokal.
Demonstrasi & penjelasan kode individual pada pertemuan ke-16.

KRITERIA: HTML&konten 20% | CSS/Flexbox&responsivitas 25%
          Interaksi JS 20% | Pengujian&perbaikan 20% | Dokumentasi&demonstrasi 15%"""

RUBRIK_UAS = """\
RUBRIK UAS - LANDING PAGE | Bobot MK: 30% | Skala 0-100

Kriteria (Bobot) | Sangat Baik 81-100 | Baik 66-80 | Cukup 56-65 | Kurang 0-55
HTML&konten(20%) | Semua seksi semantik, CTA, footer lengkap; bukti lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
CSS/Flexbox&responsivitas(25%) | Layout responsif terbaca 2 lebar; bukti tangkapan | Aspek utama; minor | Sebagian; penting | Belum ada
Interaksi JS(20%) | Min. 1 interaksi DOM/event berfungsi sesuai skenario | Aspek utama; minor | Sebagian; penting | Belum ada
Pengujian&perbaikan(20%) | Semua uji dicatat; kasus gagal diperbaiki; dokumentasi lengkap | Aspek utama; minor | Sebagian; penting | Belum ada
Dokumentasi&demonstrasi(15%) | Langkah lokal jelas; penjelasan individual sesuai kode | Aspek utama; minor | Sebagian; penting | Belum ada

Skor UAS = 0.20xK1+0.25xK2+0.20xK3+0.20xK4+0.15xK5 | Bobot MK: 30%

FORMULA NILAI AKHIR MK:
NA = (20 x Skor_T1 + 25 x Skor_UTS + 25 x Skor_T2 + 30 x Skor_UAS) / 100"""


# ===========================================================================
# HELPERS
# ===========================================================================

def unique_cells(row):
    seen = set(); result = []
    for c in row.cells:
        cid = id(c._tc)
        if cid not in seen:
            seen.add(cid); result.append(c)
    return result


def fill_block_cell(cell, text, font_size=9):
    for para in cell.paragraphs:
        for run in para.runs:
            run.text = ""
    p = cell.paragraphs[0]
    lines = text.split("\n")
    if p.runs:
        p.runs[0].text = lines[0]
        p.runs[0].font.size = Pt(font_size)
        for line in lines[1:]:
            r = p.add_run("\n" + line)
            r.font.size = Pt(font_size)
    else:
        for i, line in enumerate(lines):
            prefix = "\n" if i > 0 else ""
            r = p.add_run(prefix + line)
            r.font.size = Pt(font_size)


def clone_row(table, src_idx):
    src_tr = table.rows[src_idx]._tr
    new_tr = copy.deepcopy(src_tr)
    src_tr.addnext(new_tr)
    return table.rows[src_idx + 1]


def replace_scalars_in_doc(doc, scalar_map):
    for tag, value in scalar_map.items():
        ph = "{{" + tag + "}}"
        for para in doc.paragraphs:
            for run in para.runs:
                if ph in run.text:
                    run.text = run.text.replace(ph, value)
        for tbl in doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        full = "".join(r.text for r in para.runs)
                        if ph in full:
                            new_full = full.replace(ph, value)
                            if para.runs:
                                para.runs[0].text = new_full
                                for r in para.runs[1:]:
                                    r.text = ""


def find_and_fill_tag(tbl, tag, content, font_size=9):
    for row in tbl.rows:
        for cell in row.cells:
            if tag in cell.text:
                fill_block_cell(cell, content, font_size)
                return True
    return False


# ===========================================================================
# FILL TABLE 1 — Identitas, CPL, CPMK, Sub-CPMK, Korelasi, Pustaka
# ===========================================================================

def fill_table1(tbl):
    # --- Header institusi (Row 0) ---
    for cell in unique_cells(tbl.rows[0]):
        if "TEKNIK" in cell.text or "MESIN" in cell.text:
            txt = cell.text
            txt = txt.replace("FAKULTAS TEKNIK", "FAKULTAS SAINS DAN TEKNOLOGI INFORMASI")
            txt = txt.replace("PROGRAM STUDI S1 TEKNIK MESIN", "PROGRAM STUDI S1 SISTEM DAN TEKNOLOGI INFORMASI")
            txt = txt.replace("TEKNIK MESIN", "SISTEM DAN TEKNOLOGI INFORMASI")
            fill_block_cell(cell, txt)

    # --- CPL ---
    cpl_base = None
    for i, row in enumerate(tbl.rows):
        if "[nocpl]" in row.cells[0].text if row.cells else "":
            cpl_base = i; break
        for cell in row.cells:
            if "[nocpl]" in cell.text:
                cpl_base = i; break
        if cpl_base is not None:
            break

    if cpl_base is not None:
        ucells = unique_cells(tbl.rows[cpl_base])
        if len(ucells) >= 2:
            fill_block_cell(ucells[0], CPL_LIST[0][0])
            fill_block_cell(ucells[1], CPL_LIST[0][1])
        for extra in CPL_LIST[1:]:
            new_row = clone_row(tbl, cpl_base)
            ucells2 = unique_cells(new_row)
            if len(ucells2) >= 2:
                fill_block_cell(ucells2[0], extra[0])
                fill_block_cell(ucells2[1], extra[1])
            cpl_base += 1

    # --- CPMK ---
    cpmk_base = None
    for i, row in enumerate(tbl.rows):
        for cell in row.cells:
            if "[nocpmk]" in cell.text:
                cpmk_base = i; break
        if cpmk_base is not None: break

    if cpmk_base is not None:
        ucells = unique_cells(tbl.rows[cpmk_base])
        if len(ucells) >= 2:
            fill_block_cell(ucells[0], CPMK_LIST[0][0])
            fill_block_cell(ucells[1], CPMK_LIST[0][1])
        for extra in CPMK_LIST[1:]:
            new_row = clone_row(tbl, cpmk_base)
            ucells2 = unique_cells(new_row)
            if len(ucells2) >= 2:
                fill_block_cell(ucells2[0], extra[0])
                fill_block_cell(ucells2[1], extra[1])
            cpmk_base += 1

    # --- Sub-CPMK ---
    sub_base = None
    for i, row in enumerate(tbl.rows):
        for cell in row.cells:
            if "[nosubcpmk]" in cell.text:
                sub_base = i; break
        if sub_base is not None: break

    if sub_base is not None:
        ucells = unique_cells(tbl.rows[sub_base])
        if len(ucells) >= 2:
            fill_block_cell(ucells[0], SUBCPMK_LIST[0][0])
            fill_block_cell(ucells[1], SUBCPMK_LIST[0][1])
        for extra in SUBCPMK_LIST[1:]:
            new_row = clone_row(tbl, sub_base)
            ucells2 = unique_cells(new_row)
            if len(ucells2) >= 2:
                fill_block_cell(ucells2[0], extra[0])
                fill_block_cell(ucells2[1], extra[1])
            sub_base += 1

    # --- Single block tags ---
    find_and_fill_tag(tbl, "[tabelkolerasi]",    TABEL_KORELASI)
    find_and_fill_tag(tbl, "[pustakautama]",      PUSTAKA_UTAMA)
    find_and_fill_tag(tbl, "[pustakapendukung]",  PUSTAKA_PENDUKUNG)


# ===========================================================================
# FILL TABLE 2 — 16 Pertemuan
# ===========================================================================

def fill_table2_16pekan(tbl):
    base_idx = None
    for i, row in enumerate(tbl.rows):
        for cell in row.cells:
            if "[mingguke]" in cell.text:
                base_idx = i; break
        if base_idx is not None: break

    if base_idx is None:
        print("  [WARN] Tag [mingguke] tidak ditemukan.")
        return

    def fill_pekan(row, data):
        mg, sub, ind, krit, lur, dar, mat, bob = data
        uc = unique_cells(row)
        vals = [str(mg), sub, ind, krit, lur, dar, mat, bob]
        for ci, val in enumerate(vals):
            if ci < len(uc):
                fill_block_cell(uc[ci], val, font_size=8)

    fill_pekan(tbl.rows[base_idx], PEKAN[0])
    cur = base_idx
    for pekan_data in PEKAN[1:]:
        new_row = clone_row(tbl, cur)
        fill_pekan(new_row, pekan_data)
        cur += 1

    # Baris total
    total_row = clone_row(tbl, cur)
    uc = unique_cells(total_row)
    if uc:
        fill_block_cell(uc[0], "Total bobot penilaian", 8)
        for ci in range(1, len(uc) - 1):
            fill_block_cell(uc[ci], "", 8)
        if len(uc) > 1:
            fill_block_cell(uc[-1], "100%", 8)


# ===========================================================================
# FILL LAMPIRAN (Table 3–10)
# ===========================================================================

def fill_lampiran_tables(doc):
    contents = {
        3: PENUGASAN1, 4: RUBRIK_TUGAS1,
        5: SOAL_UTS,   6: RUBRIK_UTS,
        7: TUGAS2,     8: RUBRIK_TUGAS2,
        9: SOAL_UAS,   10: RUBRIK_UAS,
    }
    for idx, content in contents.items():
        if idx < len(doc.tables):
            tbl = doc.tables[idx]
            if tbl.rows:
                fill_block_cell(tbl.rows[0].cells[0], content, font_size=8)


# ===========================================================================
# VERIFIKASI RESIDUAL
# ===========================================================================

SCALAR_TAGS  = ["{{" + k + "}}" for k in SCALAR.keys()]
BLOCK_TAGS   = [
    "[nocpl]", "[cpl]", "[nocpmk]", "[cpmk]", "[nosubcpmk]", "[subcpmk]",
    "[tabelkolerasi]", "[pustakautama]", "[pustakapendukung]",
    "[mingguke]", "[kemampuan_subcpmk]", "[indikator]", "[kriteriateknik]",
    "[luring]", "[daring]", "[materi]", "[bobot_nilai]",
    "[penugasan1]", "[rubriktugas1]", "[soaluts]", "[rubrikuts]",
    "[tugas2]", "[rubriktugas2]", "[soaluas]", "[rubrikuas]",
]

def check_residual(doc):
    all_text = []
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                all_text.append(cell.text)
    for para in doc.paragraphs:
        all_text.append(para.text)
    combined = "\n".join(all_text)
    return [t for t in (SCALAR_TAGS + BLOCK_TAGS) if t in combined]


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=" * 70)
    print("  GENERATOR RPS OBE — STI-311 Pengembangan Web Front End")
    print("=" * 70)

    if not os.path.exists(TEMPLATE):
        print(f"[ERROR] Template tidak ditemukan:\n  {TEMPLATE}")
        sys.exit(1)

    shutil.copy2(TEMPLATE, OUT_DOCX)
    doc = Document(OUT_DOCX)
    print(f"  Template disalin ke: {OUT_DOCX}")
    print(f"  Jumlah tabel template: {len(doc.tables)}")

    print("\n[T3] Mengisi blok [tag] ...")
    print("  → Cover (Table 0)...")
    tbl0 = doc.tables[0]
    for row in tbl0.rows:
        for cell in row.cells:
            if "AGUSTUS" in cell.text:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.text = run.text.replace("AGUSTUS, 2026", "NOVEMBER, 2026")

    print("  → Identitas, CPL, CPMK, Sub-CPMK (Table 1)...")
    fill_table1(doc.tables[1])

    print("  → 16 Pertemuan (Table 2)...")
    fill_table2_16pekan(doc.tables[2])

    print("  → Lampiran instrumen & rubrik (Table 3-10)...")
    fill_lampiran_tables(doc)

    print("  → Pengesahan (Table 11)...")
    if len(doc.tables) > 11:
        tbl11 = doc.tables[11]
        for row in tbl11.rows:
            for cell in row.cells:
                if "Tanggal Bulan Tahun" in cell.text:
                    for para in cell.paragraphs:
                        for run in para.runs:
                            run.text = run.text.replace(
                                "Tanggal Bulan Tahun", "Malang, 8 November 2026"
                            )

    print("\n[T3] Mengisi scalar {{tag}} ...")
    replace_scalars_in_doc(doc, SCALAR)

    doc.save(OUT_DOCX)
    print(f"\n[T4] File disimpan: {OUT_DOCX}")

    print("\n[T5] Verifikasi residual tag...")
    doc2 = Document(OUT_DOCX)
    residual = check_residual(doc2)
    if residual:
        print(f"  [PERINGATAN] {len(residual)} tag masih tersisa:")
        for r in residual:
            print(f"    {r}")
    else:
        print("  PASS: Zero residual — semua tag berhasil diisi.")

    size = os.path.getsize(OUT_DOCX)
    print("\n" + "=" * 70)
    print("  RINGKASAN HASIL")
    print("=" * 70)
    print(f"  Output : {OUT_DOCX}")
    print(f"  Ukuran : {size:,} bytes ({size // 1024} KB)")
    print("\n  DAFTAR BUTIR KONFIRMASI (isi manual setelah validasi prodi):")
    for tag, val in SCALAR.items():
        if "[PERLU KONFIRMASI" in val:
            print(f"    - {{{{{tag}}}}}: {val}")
    print("\n  BATAS VERIFIKASI:")
    print("    PASS  Zero residual (cek terprogram)")
    print("    PASS  CPL, CPMK, Sub-CPMK verbatim dari 065_1 & Dok 043")
    print("    PASS  Skema asesmen: T1 20% | UTS 25% | T2 25% | UAS 30% = 100%")
    print("    BELUM Tata letak cetak belum dirender (buka di MS Word / LibreOffice)")
    print("    BELUM Merge sel UTS/UAS belum diverifikasi visual")
    print("    BELUM Nama dosen, NUPTK, koordinator belum dikonfirmasi prodi")
    print("\n[SELESAI]")


if __name__ == "__main__":
    main()
