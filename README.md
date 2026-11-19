# Kurikulum OBE SISTEKIN 2026 — Indeks Repositori

Repositori kerja penyusunan Kurikulum OBE Program Studi **Sistem dan Teknologi Informasi (S1)**, Fakultas Sains dan Teknologi Informasi, Universitas Widyagama Malang.

> **Status:** dokumen merupakan bahan kerja kurikulum. Keberadaan berkas, hasil pemeriksaan otomatis, dan nama `FINAL` pada berkas tidak dengan sendirinya menunjukkan pengesahan akademik. Periksa status dan catatan pengesahan masing-masing dokumen.

## Mulai di sini

| Kebutuhan | Tautan | Peran |
|---|---|---|
| Indeks lengkap dokumen dan paket per mata kuliah | [Indeks Markdown](KURIKULUM2026_REVISI/INDEX.md) | Navigasi ke dokumen induk dan lima berkas setiap MK. |
| Struktur, nama, kode, SKS, semester dan prasyarat | [Dokumen 005](KURIKULUM2026_REVISI/005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md) | Rujukan utama identitas Kurikulum 2026. |
| CPMK, Sub-CPMK dan rencana pembelajaran | [Dokumen 007](KURIKULUM2026_REVISI/007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md) | Formulasi dan silabus mata kuliah. |
| CPL, CPMK, BoK dan batas materi | [Dokumen 043 induk](KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md) · [Dokumen 037](KURIKULUM2026_REVISI/037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md) | Matriks dan batas antar-MK. |
| Rencana dan rubrik perangkat ajar | [Manifest perangkat ajar](KURIKULUM2026_REVISI/PERANGKAT_AJAR/README.md) | Penomoran `055`–`100` dan aturan penempatan. |
| Revisi Web Front End | [Rancangan STI-311](KURIKULUM2026_REVISI/043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md) · [Audit dampak](KURIKULUM2026_REVISI/LAPORAN_AUDIT_DAMPAK_STI-311.md) | Lingkup baru dan pekerjaan validasi MK hilir. |
| Akses bacaan web | [Portal HTML](KURIKULUM2026_REVISI/index.html) | Navigasi tambahan; perhatikan peringatan versi pada portal. |
| Aturan untuk kontributor dan agent | [AGENTS.md](AGENTS.md) | Ketentuan proyek, sumber, dan alur kerja. |
| Akses dokumen SiTI/SISTEKIN dari repo GitHub sumber | [Skill `kurikulum-github-access`](.opencode/skills/kurikulum-github-access/SKILL.md) | Menemukan, membaca, dan mengutip dokumen `KURIKULUM2026_REVISI/` dari repo `roniwahyu/--BRAINSTORMING_KURIKULUM2026`. |
| Penyusunan LED, LKPS, dan instrumen akreditasi Sarjana | [Skill `led-akreditasi-sarjana`](.opencode/skills/led-akreditasi-sarjana/SKILL.md) | Peta indikator LAM INFOKOM 2.1 untuk Status Terakreditasi, templat pengisian, dan reviu bukti. |

Contoh prompt untuk agent:

- “Gunakan `kurikulum-github-access` untuk mencari RPS STI-102 Kurikulum 2026 dan berikan tautan berkas sumbernya.”
- “Gunakan `led-akreditasi-sarjana` untuk menjelaskan butir 1a–1e dan membuat matriks bukti PPEPP untuk SISTEKIN.”

## Struktur repositori

```text
KURIKULUM2026_REVISI/          Dokumen kurikulum aktif dan bahan kerja
├── INDEX.md                   Indeks dokumen dan paket MK, dapat diperbarui dengan skrip
├── 003 / 004 / 005 / 007...  Dokumen induk OBE dan struktur kurikulum
├── 037 / 043...               Boundary, matriks, dan rancangan STI-311
├── PERANGKAT_AJAR/            RPS, SAP, outline, asesmen, dan rubrik
├── _tools/                    Pemeriksaan dan generator
├── HTML/                      Portal dan salinan HTML yang dihasilkan sebelumnya
├── PDF/ dan DOCX/             Ekspor; versinya perlu diverifikasi
└── assets/                    Aset dokumen dan ilustrasi
KURIKULUM2025/                 Dokumen referensi kurikulum 2025
KURIKULUM2026_ZCODE/           Dokumen analisis awal/historis
KURIKULUM2026_REVISI_OPUS5/    Bahan kerja alternatif
BUKU_OBE/                      Referensi buku dan panduan OBE
SURVEY_PEMETAAN2026/           Bahan riset, survei, dan pemetaan
AGENTS.md                      Instruksi dan sumber kerja proyek
```

Untuk data Kurikulum 2025, rujuk [laporan resmi SIAKAD](<KURIKULUM2025/Laporan%20Daftar%20Kurikulum%20Prodi%20Sistekin.pdf>); jangan mengganti sumber primer dengan draft analisis lama. Analisis lama `analisis_vmts_sistekin.md` dan `analisis_mk_sistekin.md` menggunakan metode pembobotan yang tidak tervalidasi; **jangan gunakan skor 47,5%, 57,1% atau 100% dari kedua dokumen tersebut** sebagai kesimpulan akreditasi. Arah AI/Smart Systems + Technopreneurship merujuk keputusan rapat 9 Juni 2026.

## Statistik beban studi yang disampaikan

| Komponen | SKS | Jumlah MK | Keterangan |
|---|---:|---:|---|
| MKU — wajib universitas | 14 | 8 | Termasuk 2 MK masing-masing 0 SKS |
| FSTI — wajib fakultas | 36 | 14 | Termasuk Pengantar AI 2 SKS |
| STI — wajib prodi | 93 | 30 | |
| **Total wajib** | **143** | **52** | |
| Pilihan peminatan yang diambil | 27 | 9 | Masing-masing 3 SKS |
| **Total syarat graduasi** | **170** | **61** | |

> **Perlu rekonsiliasi:** statistik di atas disampaikan untuk pembaruan README dan belum selaras dengan [Dokumen 005](KURIKULUM2026_REVISI/005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md), yang saat ini mencatat **146 SKS / 55 MK ditempuh**. Perbedaan komponen dan angka kelulusan perlu ditinjau RMK/prodi sebelum dijadikan ketentuan resmi atau diselaraskan ke dokumen kurikulum lainnya. Dokumen 005 belum diubah dalam pembaruan ini.

## Ringkasan status

- Dokumen 005 juga mencatat portofolio **67 MK / 182 SKS** yang ditawarkan; angka ini bukan jumlah paket perangkat ajar yang sudah tersedia.
- Nomor `055`–`100`: **46 MK Core STI dan pilihan STA/STB/STC**, masing-masing lima Markdown (230 berkas). Berkas tersedia belum berarti mutu dan pengesahannya sudah selesai.
- Paket `113` untuk **FST-714 Skripsi / Tugas Akhir** juga tersedia dalam lima Markdown, tetapi berada di luar hitungan 46 MK tersebut. Jangan menganggap seluruh FST/MKU sudah memiliki paket.
- Revisi **STI-311** diselaraskan pada dokumen Markdown terkait: HTML/CSS dasar–menengah, Flexbox lanjutan, pengenalan Bootstrap/Tailwind dan JavaScript dasar; React/API bukan capaian STI-311 yang baru. Tinjauan dan pengesahan akademik serta keputusan penempatan materi hilir masih diperlukan.
- Salinan HTML dan ekspor XLSX/DOCX/PDF dapat berbeda dari sumber Markdown. Ekspor yang belum diregenerasi atau diverifikasi **tidak boleh diasumsikan mutakhir**. Dokumen backup/pilot lama dipertahankan sebagai arsip.

## Memperbarui dan memeriksa indeks

Dari root repositori:

```bash
python3 -B KURIKULUM2026_REVISI/_tools/update_markdown_index.py
python3 -B KURIKULUM2026_REVISI/_tools/update_markdown_index.py --check
python3 -B KURIKULUM2026_REVISI/_tools/convert_md_to_html.py --index-only
python3 -B KURIKULUM2026_REVISI/_tools/verify_sti311_alignment.py
python3 -B KURIKULUM2026_REVISI/_tools/verify_perangkat_ajaran_peminatan_sem7.py
```

`--index-only` hanya memperbarui portal dan tidak mengonversi dokumen HTML. Konversi penuh membutuhkan paket Python `markdown` dan tidak otomatis membuktikan keselarasan isi.

Pemeriksaan identitas terhadap Dokumen 005 dijalankan dari folder `KURIKULUM2026_REVISI/`:

```bash
python3 -B _tools/verify_all_mk_aligned_with_005.py
python3 -B _tools/verify_zero_discrepancy.py
python3 -B _tools/check_all_md_alignment_with_005.py
```

Pemeriksaan ini membantu menemukan diskrepansi tertentu, tetapi tidak menggantikan audit substansi, peninjauan koordinator, atau pengesahan prodi. Perangkat ajar baru atau hasil pengayaan dibuat langsung di `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`, sesuai [manifest](KURIKULUM2026_REVISI/PERANGKAT_AJAR/README.md).
