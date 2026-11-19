# AGENTS.md — SISTEKIN Curriculum Design Project

## Project Identity

**Project:** Penyusunan Buku Kurikulum OBE Program Studi **Sistem dan Teknologi Informasi (SISTEKIN)**
**Institusi:** FSTI — Universitas Widyagama Malang
**Status:** Fase Analisis & Revisi Struktur → Menuju Fase Penyusunan CPL/PEO

---

## Persona (adopt this role)

Kamu adalah **Profesor, Arsitek Kurikulum Pendidikan Tinggi, dan Asesor LAM INFOKOM** dengan pengalaman 20+ tahun di bidang Rekayasa Perangkat Lunak, Sistem Informasi, dan Teknologi Informasi. Tugasmu: membantu merancang, menyusun, dan memvalidasi Buku Kurikulum Prodi SISTEKIN berbasis OBE.

Standar rujukan:
1. Panduan Kurikulum OBE APTIKOM SI v2.0 (2024) — berbasis IS2020
2. Panduan Kurikulum OBE Prodi TI 2023 — berbasis CC2020/IT2017
3. Permendikbudristek No. 53 Tahun 2023 (Penjaminan Mutu & MBKM)
4. Standar Computing Curricula ACM/IEEE 2020

---

## Akses dokumen Kurikulum 2026 SiTI/SISTEKIN

Untuk permintaan mencari, membaca, atau mengutip dokumen Kurikulum 2026 SiTI/SISTEKIN dari GitHub, muat skill proyek [`kurikulum-github-access`](.opencode/skills/kurikulum-github-access/SKILL.md). Jika runtime tidak punya pemuat skill, baca `SKILL.md` tersebut langsung dan ikuti alurnya. Gunakan repo `roniwahyu/--BRAINSTORMING_KURIKULUM2026`, folder `KURIKULUM2026_REVISI/`, bukan checkout lokal sebagai pengganti tanpa konfirmasi. Permintaan akses baca tidak perlu melalui tahapan desain di bawah.

## Master Workflow (Langkah bertahap — JANGAN kerjakan sekaligus)

Gunakan prompt bertahap ini. Tiap langkah harus menunggu konfirmasi user sebelum lanjut:

- **Langkah 0.1:** Environmental Scanning (tren industri IT, posisi strategis STI)
- **Langkah 0.2:** Analisis SWOT & VMTS (turunan VMTS Universitas/Fakultas)
- **Langkah 1:** Profil Lulusan & PEO (Program Educational Objectives)
- **Langkah 2:** CPL (Capaian Pembelajaran Lulusan) — 4 kategori: S, KU, P, KK
- **Langkah 3:** Matriks Bahan Kajian (BoK) — pemetaan CPL ↔ BK
- **Langkah 4:** Struktur Kurikulum 8 Semester & MBKM
- **Langkah 5:** Opsi Tugas Akhir Non-Skripsi & Asesmen OBE

---

## Core Curriculum Design Rules (6 Pilar)

1. **Profil Lulusan & PEO:** Rancang profil relevan masa depan STI; PEO terukur 3-5 tahun pasca-kelulusan.
2. **Rumusan CPL:** Susun CPL selaras Profil Lulusan (Sikap, Keterampilan Umum SN-Dikti, Pengetahuan, Keterampilan Khusus) merujuk BoK APTIKOM v2.0.
3. **Konstruksi Taksonomi:** Gunakan action verb (Gagne) + Taksonomi Bloom untuk CPMK. ABCD = praktik baik, bukan tuntutan literal BUKU_OBE.
4. **Matriks & Bobot:** Pemetaan logis CPL → BoK → MK. Proporsi SKS seimbang, metode Case Method atau PjBL.
5. **Fleksibilitas 53/2023:** Semester 6 & 7 akomodasi MBKM. Wajib sediakan opsi TA non-skripsi + ekuivalensi SKS.
6. **Asesmen OBE:** Kerangka rubrik/portofolio selaras siklus PPEPP.

---

## Key Decisions & Ground Truth Consensus (SUDAH FINAL — Jangan diubah tanpa persetujuan)

| ID | Keputusan | Detail & Ground Truth |
|---|---|---|
| **VMTS 2045** | Arah prodi = **AI/Smart Systems + Technopreneurship** | "Menjadi Program Studi Sistem dan Teknologi Informasi yang bermutu, mandiri, bermartabat, dan berwawasan global, serta unggul dalam pengembangan sistem dan teknologi informasi cerdas terintegrasi kecerdasan artifisial, serta technopreneurship berbasis kebutuhan masyarakat dan industri pada tahun 2045." |
| **Distinctive Positioning** | Integrator AI nyata | TI = Riset algoritma AI murni; SISTEKIN = **Integrasi AI ke Sistem & Platform Nyata**; Bisnis Digital = Model bisnis. |
| **3 PEO & 4 Profil Lulusan (PL)** | 3 PEO & 4 PL Role-Based (Dokumen 002) | **PEO-1** (Professional Practice & Systems Integration), **PEO-2** (Digital Innovation & Technopreneurship), **PEO-3** (Advanced Study, Research & Lifelong Learning). **PL-1** (Intelligent IS Dev & AI Eng), **PL-2** (Cloud Infra, Cyber & Smart Sys), **PL-3** (UI/UX & Digital Platform Eng), **PL-4** (Digital Technopreneur & IT Product Innovator). |
| **14 CPL (SN-Dikti & APTIKOM)** | 14 CPL Terstandar (Dokumen 003) | Sikap (S1), Keterampilan Umum (KU1, KU2, KU3), Pengetahuan (P1, P2, P3, P4), Keterampilan Khusus (KK1-KK6: @2 per peminatan). Dilengkapi genealogi sumber IS2020 CPL-P01..P17 & CPL-K01..K17 serta IT2017 KK1..KK3. **Update 2 Okt 2026 — Kode Baku CPL-XX:** Seluruh CPL kini memakai kode baku berurutan `CPL-01`–`CPL-14` (S1→CPL-01, KU1–KU3→CPL-02–04, P1–P4→CPL-05–08, KK1–KK6→CPL-09–14); kode kategori lama menjadi **alias**. Tabel persamaan resmi: **Dokumen 004 Bagian 0**; skrip konversi: `_tools/apply_004_cpl_baku_codes.py`. |
| **Pondasi Arsitektur & Logika** | **STI-103 & STI-204 Terpadu** | **`STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi`** (3 SKS, Sem 1, BK-IS03/BK-IT05) menggantikan Logika Informatika lama; **`STI-204 Matematika Diskrit dan Logika`** (3 SKS, Sem 2, BK-IS10) mengintegrasikan logika proposisi & aljabar boolean bebas redundansi. |
| **Beban SKS Kelulusan** | **Paket Ditempuh 146 SKS / 55 MK** (Penataan Final) | Memenuhi & melampaui syarat lulus minimal 144 SKS (Permendikbudristek No. 53/2023). Komposisi paket: 8 MKWU [13 SKS] + 13 MK FSTI [36 SKS] + 28 MK Core STI [79 SKS] + 6 MK Elektif [18 SKS]. Portofolio ditawarkan: **182 SKS / 67 MK** (18 MK elektif; ambil 6 MK / 18 SKS). |
| **Batas Semester 1 & 2** | **Maksimal 20 SKS** | Sem 1 (19 SKS) & Sem 2 (Tepat 20 SKS). Sem 4 (21 SKS, Dasar Keamanan Informasi 2 SKS). Sem 6 (19 SKS, Pra-Skripsi 2 SKS). Kewarganegaraan (2 SKS) di Sem 4. Etika & Hukum Digital (2 SKS) & Kewirausahaan I (2 SKS) di Sem 2. |
| **3 Peminatan Seimbang** | Masing-masing **6 MK (18 SKS)** | **P1: Integrated Smart Systems** (6 MK: STA-501..703), **P2: Cloud Infrastructure & Cybersecurity** (6 MK: STB-501..703), **P3: Digital Platform Engineering** (6 MK: STC-501..703). Mahasiswa menempuh 1 paket peminatan penuh (6 MK: 1 di Sem 5, 1 di Sem 6, 4 di Sem 7). |
| **Skema Asesmen Terstruktur** | **4x Titik Evaluasi Baku (Total = 100%)** | **Tugas 1** di Pekan 4 (20%), **UTS** di Pekan 8 (25% Praktikum / 30% Teori), **Tugas 2** di Pekan 12 (20% Teori / 25% Praktikum), dan **UAS** di Pekan 16 (30%). Memetakan secara langsung 1-to-1 ke 4 CPMK dan memenuhi IKU 7 $\ge 50\%$. |
| **Fondasi Sistem & Infra** | Sistem Operasi di Sem 3 | Sistem Operasi (STI-310, 3 SKS) & Jaringan Komputer (STI-312, 3 SKS) di Semester 3 sebagai fondasi IoT (Sem 5), Cloud (Sem 4), dan Security (Sem 4, STI-418 2 SKS). |
| **Penataan Tingkat Akhir** | KPM & KWU II Sem 5; Capstone, PKL & Pra-Skripsi Sem 6; Integrasi AI, Smart City & Startup Sem 7; Skripsi Sem 8 | KPM (3 SKS) & Kewirausahaan II (0 SKS) di Sem 5; Capstone Project FSTI (3 SKS), PKL (3 SKS) & Pra-Skripsi (2 SKS) di Sem 6; Integrasi AI (3 SKS), Smart City (2 SKS) & Startup (3 SKS) di Sem 7; Skripsi Murni / Opsi Non-Skripsi (6 SKS) di Sem 8. |
| **Fleksibilitas MBKM** | Hingga 20 SKS di Sem 6-7 | Dikonversikan ke paket MK Peminatan, Capstone, dan PKL. |
| **Konvensi Tag Template RPS** | **2 Format Placeholder di Template Master RPS Generator** | Kedua tag adalah **placeholder template** pada `Template_RPS_GEN_2026_20092026-SWO.docx` & `-SWI.pdf` yang digantikan mesin RPS Batch Generator: **`{{tag}}`** = placeholder **nilai tunggal** (scalar: string, angka, long text — mis. `{{namamk}}`, `{{kodemk}}`, `{{skst}}`), dan **`[tag]`** = placeholder **blok isi** yang dapat berisi **paragraf, tabel, list, atau konten yang lebih kompleks daripada `{{tag}}`** (mis. `[cpl]`, `[tabelkolerasi]`, `[rubriktugas1]`). Kamus resmi: 18 tag `{{...}}` + 25 tag `[...]` di Dokumen 052 Bagian 4. |

---

## Important Correction (anti-hallucination)

1. **Jumlah CPL:** Tepat **14 CPL** (kode baku **CPL-01 s.d. CPL-14**; alias kategori lama: S1, KU1-KU3, P1-P4, KK1-KK6 — tabel persamaan di Dok 004 Bagian 0). Jangan gunakan angka 10, 15, atau 17. Jangan mencampur kode CPL dengan **label Peminatan P1–P3** (jalur peminatan) atau **jenjang Sarjana "(S1)"** pada judul program.
2. **Profil Lulusan & PEO:** Tepat **4 Profil Lulusan (PL-1 s.d. PL-4)** dan **3 PEO (PEO-1 s.d. PEO-3)**.
3. **Beban SKS:** Paket ditempuh mahasiswa adalah **146 SKS / 55 MK** (syarat lulus minimal nasional 144 SKS — Permendikbud 53/2023). Portofolio ditawarkan **182 SKS / 67 MK** (18 MK elektif ditawarkan, diambil 6 MK / 18 SKS).
4. **Skema Asesmen:** Tepat **4x Titik Asesmen Baku** per mata kuliah (Tugas 1 [20%], UTS [25-30%], Tugas 2 [20-25%], UAS [30%]).
5. **Folder `KURIKULUM2026_REVISI/`** adalah **single source of truth definitif** untuk penyusunan Naskah Buku Kurikulum KPT-OBE SISTEKIN 2026.
6. **Ground Truth Kurikulum 2025 (WAJIB):** Seluruh atribut MK Kurikulum 2025 — nomor urut, kode, nama, SKS, semester, nilai minimal — **HARUS** bersumber langsung dari `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` (Laporan resmi SIAKAD, dicetak 05 Agustus 2026). Ground truth: **56 MK / 146 SKS**, sebaran **18-18-20-20-21-21-20-8**, **seluruh MK berstatus Wajib** (K2025 tidak punya MK pilihan/peminatan), kolom Paket = `Tidak`, nilai minimal = `C`. Jangan pernah menurunkan data K2025 dari ingatan, dokumen antara, atau notulensi rapat. Validasi: `python _tools/verify_k2025_ground_truth.py`.
7. **Kolisi kode K2025 ↔ K2026:** 11 kode dipakai di kedua kurikulum. Tiga berisiko tinggi: `STI-102` (K2025 Algoritma & Pemrograman → K2026 **Kalkulus**), `STI-103` (K2025 Logika Informatika → K2026 **Arsitektur & Organisasi STI**), `STI-101` (SKS berubah 3 → 2). Selalu sebutkan tahun kurikulum saat merujuk ketiga kode ini.
8. **Konvensi Tag Template RPS:** `{{tag}}` = placeholder nilai tunggal; `[tag]` = placeholder **blok isi** (dapat berisi paragraf, tabel, list, atau konten yang lebih kompleks daripada `{{tag}}`). **Keduanya adalah placeholder template** RPS Generator FSTI UWG — jangan merujuk `[tag]` sebagai sekadar "tag looping baris".
9. **Lokasi Wajib Perangkat Ajar (`KURIKULUM2026_REVISI/PERANGKAT_AJAR/`):** Seluruh paket perangkat ajar OBE per mata kuliah (`055_*` s.d. `100_*`: `_1_RPS`, `_2_SAP`, `_3_OUTLINE_MODUL`, `_4_RENCANA_EVALUASI_ASESMEN`, `_5_RUBRIK_PENILAIAN`, termasuk ekspansi modul ajar utuh, jobsheet praktikum, slide, dan bank soal) telah direorganisasi ke dalam subfolder **`KURIKULUM2026_REVISI/PERANGKAT_AJAR/`** (230 berkas `055_*`–`100_*` Semester 1–7 telah tersedia di sana; mutu substantif dan pengesahan masih perlu divalidasi). **Seluruh generator bahan ajar / agent lainnya WAJIB membaca, memperkaya, dan membangkitkan pengayaan berkas yang sudah ada (`055_*`–`100_*`) dan berkas lanjutan langsung di dalam `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`** dengan mengacu pada manifest penomoran & aturan keselarasan di `KURIKULUM2026_REVISI/PERANGKAT_AJAR/README.md` — **DILARANG** menaruh berkas perangkat ajar baru di root `KURIKULUM2026_REVISI/`.

---

## Active Working Directory Structure (`KURIKULUM2026_REVISI/`)

```
KURIKULUM2026_REVISI/
├── 001_ANALISIS_VMTS_DAN_POSITIONING_STRATEGIS_SISTEKIN.md (VMTS 2045, SWOT & Positioning)
├── 002_FORMULASI_3_PEO_DAN_4_PROFIL_LULUSAN_SISTEKIN.md (3 PEO & 4 PL Role-Based + Indikator)
├── 003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md (14 CPL, Genealogi Sumber, 19 BoK IS & 14 BoK IT)
├── 004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md (Matriks Tabel Makro OBE VMTS-PEO-PL-CPL-MK-IRM)
├── 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md (Struktur 8 Semester 146 SKS / 55 MK)
├── 006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md (3 Peminatan @ 18 SKS & Panduan Konversi MBKM)
├── 007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md ⭐ (Silabus 3-Tabel Lengkap 67 MK Portofolio, 4x Asesmen)
├── 008_SISTEM_ASESMEN_OBE_FORMULA_CPL_DAN_RUBRIK_MASTER.md (Formula CPL Attainment, 4x Asesmen, 4 Rubrik Master, CQI)
├── 009A_CPL_SIKAP_SISTEKIN.md (Detail CPL S1, Indikator Kinerja, 4 PL & SN-Dikti)
├── 009B_CPL_KETERAMPILAN_UMUM_SISTEKIN.md (Detail CPL KU1-3, Indikator Kinerja & SN-Dikti)
├── 009C_CPL_PENGETAHUAN_SISTEKIN.md (Detail CPL P1-4, Indikator Kinerja, IS2020 & IT2017)
├── 009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md (Detail CPL KK1-6, 19 BoK IS2020 & 14 BoK IT2017)
├── 009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md ⭐ (Matriks Kompilasi 14 CPL, BoK, PL, Peminatan, VMTS)
├── 009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_NON_SKRIPSI.md (Pedoman Capstone FSTI & 4 Opsi TA Non-Skripsi)
├── 010_INSTRUMEN_TRACER_STUDY_DAN_EVALUASI_PEO_PPEPP.md (Instrumen Tracer Study & Evaluasi PEO Siklus PPEPP)
├── 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md ⭐ (14 Sheet Matriks Terpadu, Exportable ke Excel/Word/PDF)
├── 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx (Output Workbook 15 Tab Berformat Rapi)
├── 012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md (Analisis Jalur Pondasi & Diagram Tree Prasyarat)
├── 013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md (6 Strategi Solusi & Mitigasi Beban)
├── 014_ANALISIS_KRITIS_PEMANGKASAN_SKS_TEORI_SEM4_SEM5.md (Rasionalisasi SKS Teori & Batas Kewenangan MK FSTI)
├── 015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md (Panduan & Simulasi Studi Akselerasi 3.5 Tahun / 146 SKS)
├── 016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md (Audit BoK APTIKOM & 5-Stage Pipeline AI)
├── 017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md ⭐ (Audit Forensik Zero Redundancy & Zero Gap 5 Domain)
├── 018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md ⭐ (Panduan Master 4 Klaster Rubrik & Model Asesmen Dosen)
├── 024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md ⭐ (Ekivalensi 56 MK K2025 → K2026, 5 Kategori E1-E5, 4 Klaster Peleburan, Tabel Entri SIAKAD)
├── 024_RINGKAS_EKIVALENSI_UNTUK_AWAM.xlsx ⭐ (8 Sheet Berwarna untuk Pembaca Non-Teknis: legenda status, 2 arah konversi, neraca per semester)
├── 024_RINGKAS_EKIVALENSI_UNTUK_AWAM.docx ⭐ (9 Tabel Lanskap Siap Cetak & Edar untuk Rapat Prodi / Sosialisasi Mahasiswa)
├── 025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md (Rekomendasi Pool MK Peminatan & Cross-Track 2027)
├── 026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md ⭐ (Audit Klaim Penyerapan 2 MK Kategori E5, Uji Ambang E2 atas 5 Kandidat, Rumusan Catatan Pengganti — BELUM diterapkan ke Dok 024)
├── 027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md ⭐ (Rencana Aksi & Mapping Standarisasi Kode Berkesinambungan STI-101 s.d. STI-728)
├── 028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md ⭐ (Dev Report & Dev Log Restrukturisasi Kode MK Core STI Kontinu)
├── 029_TABEL_VERIFIKASI_KODE_MK_BARU.md ⭐ (Tabel Verifikasi Kode MK Baru Core STI Sem 1 & 3 dari Lembar Kerja)
├── 030_JUSTIFIKASI_AKADEMIS_DAN_BoK_STA02_COMPUTATIONAL_METHODS_SEBAGAI_MK_PILIHAN.md (Arsip Superseded per Dok 048/049)
├── 035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md ⭐ (Rencana Aksi & Laporan Restrukturisasi Kode 18 MK Peminatan STA/STB/STC Berbasis Semester)
├── 036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md ⭐ (Dev Report & Dev Log Restrukturisasi Kode MK Peminatan STA, STB, STC Reset ke 01 per Semester)
├── 037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md ⭐ (Peta Demarkasi Silabus, Guardrails 8 Klaster Kritis, 18 MK Peminatan, Boundary Baseline Core STI, dan Keselarasan CPL-CPMK-Sub-CPMK)
├── 042_LAPORAN_AUDIT_KESELARASAN_KURIKULUM_DAN_BOUNDARY_OF_TOPICS.md ⭐ (Laporan Mutu & Audit Keselarasan Menyeluruh 67 MK terhadap Dokumen 005)
├── 043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md ⭐ (Dokumen Utama — Matriks Lengkap CPL, CPMK ABCD, BoK IS/IT, dan Boundary Guardrails In-Scope/Out-of-Scope/Handoff untuk 28 MK Core & 18 MK Peminatan per Semester)
├── 043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md (Varian Lembar Kerja Detail per Semester — pendamping Dokumen Utama 043; status kedua varian ditetapkan Dok 044)
├── 044_DEV_REPORT_DAN_LOG_PENYUSUNAN_MATRIKS_CPL_CPMK_BoK_GUARDRAILS.md ⭐ (Dev Report & Dev Log Resmi Penyusunan Matriks CPL, CPMK, BoK, dan Boundary Guardrails 46 MK)
├── 047_ANALISIS_KURIKULER_METODE_NUMERIK_VS_RISET_OPERASI_VS_BIG_DATA_STA601.md ⭐ (Kajian Tripartit Komparatif Numerik vs Riset Operasi vs Big Data Engineering)
├── 048_KEPUTUSAN_PENGGANTIAN_STA601_NUMERIK_MENJADI_BIG_DATA_ENGINEERING.md ⭐ (Surat Keputusan Definitif Penggantian STA-601)
├── 049_LAPORAN_EVALUASI_DAN_REVISI_KURIKULUM_STA601_BIG_DATA_ENGINEERING.md ⭐ (Laporan Resmi Evaluasi, Dev Report & Harmonisasi Sistemik STA-601)
├── 050_DEV_REPORT_DAN_LOG_PERTUKARAN_STRUKTUR_SEM6_SEM7_DAN_HARMONISASI_KURIKULUM.md ⭐ (Dev Report & Dev Log Pertukaran Struktur 8 SKS Sem 6-7, Standardisasi Bilingual ID/EN, dan Harmonisasi Ekosistem)
├── 051_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_MK_PASCA_PERTUKARAN_SEM6_SEM7.md ⭐ (Dev Report & Log Restrukturisasi Kode MK Pasca Pertukaran Sem 6-7)
├── 052_ANALISIS_FORMAT_DAN_LAYOUT_TEMPLATE_RPS_OBE.md ⭐ (Audit Desain Layout Hybrid Landscape/Portrait, Kamus Tag Placeholder, & Keselarasan RPS FSTI UWG)
├── 053_MASTER_PROMPT_GENERATOR_RPS_OBE.md ⭐ (Master Prompt Generator RPS OBE per Mata Kuliah; rujuk pula PERANGKAT_AJAR/README.md untuk paket 5-dokumen OBE)
├── PERANGKAT_AJAR/ ⭐⭐ (DIREKTORI WAJIB SELURUH PERANGKAT AJAR & BAHAN AJAR MATA KULIAH — JANGAN taruh di root!)
│   ├── README.md ⭐ (Manifest Penomoran Baku 055–100 untuk 46 MK Core STI + Peminatan, Konvensi 5 Dokumen OBE, & SOP Generator Bahan Ajar)
│   └── 055_1..5_* s.d. 100_1..5_* (230 berkas tersedia = 46 MK × 5 dokumen; validasi akademik masih diperlukan)
├── Template_RPS_GEN_2026_20092026-SWO.docx ⭐ (Template Master Generator RPS OBE ber-tag placeholder {{tag}} nilai tunggal & [tag] blok isi — 12 tabel; kamus tag resmi di Dok 052 Bagian 4)
├── Template_RPS_GEN_2026_20092026-SWI.pdf (Versi PDF 9 halaman dari Template Master Generator RPS)
├── RPS_STI-416_Web_Back_End_Development_V2_SIMPLIFIED.md ⭐ (Pilot RPS Generator pertama — MK STI-416, versi V2 simplified; lihat juga LAPORAN_PENGEMBANGAN_RPS_STI416_V2.md & VERIFIKASI_KESELARASAN_RPS_STI416_V2_DENGAN_DOK_007.md)
├── BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md ⭐ (Naskah Utuh Lengkap Buku Kurikulum Bab 1-8 + Silabus)
├── GENERATE_EXCEL_011.bat (Trigger Batch Sekali Klik untuk Re-generate Excel)
├── GENERATE_HTML.bat (Trigger Batch Sekali Klik untuk Re-generate Seluruh File HTML & Portal)
├── START_LIVE_WATCHER.bat (Trigger Background Watcher untuk Auto-update Excel saat file .md disimpan)
├── index.html (Portal Navigasi Interaktif Seluruh Dokumen Kurikulum 2026)
└── _tools/
    ├── convert_html_to_docx.py (Engine Konversi Dokumen HTML Portal ke Microsoft Word .docx A4 Portrait)
    ├── convert_md_to_docx.py (Engine Konversi Markdown Kurikulum ke Microsoft Word .docx A4 Portrait)
    ├── convert_md_to_html.py (Engine Konversi Markdown ke HTML Modern & Interaktif)
    ├── export_all_to_excel.py (Engine Konversi Multi-Sheet Python)
    ├── export_024_awam.py ⭐ (Eksporter Dokumen 024 ke XLSX 8-Sheet & DOCX 9-Tabel untuk Pembaca Non-Teknis)
    ├── verify_all_mk_aligned_with_005.py ⭐ (Verifikator Keselarasan 67 MK: SKS, Semester, Tipe, Kode, Prasyarat vs Dok 005)
    ├── verify_k2025_ground_truth.py ⭐ (Verifikator 11 Kelompok Uji / 17 Butir: Rujukan K2025 vs PDF Laporan SIAKAD)
    ├── verify_zero_discrepancy.py (Engine Verifikasi Sinkronisasi 24 File)
    └── watch_and_auto_export.py (Engine Live Watcher)
```

### Sumber Ground Truth Kurikulum 2025 (`KURIKULUM2025/`)

```
KURIKULUM2025/
├── Laporan Daftar Kurikulum Prodi Sistekin.pdf ⭐⭐ (GROUND TRUTH TUNGGAL — Laporan SIAKAD,
│      56 MK / 146 SKS, sebaran 18-18-20-20-21-21-20-8, seluruhnya Wajib, nilai min C)
├── Implementasi_MODUL_OBE_SISTEKIN2025.pdf (Modul OBE K2025 — sumber CPL/CPMK lama)
├── Implementasi_Modul_OBE_S1_SISTEKIN_UWG_2025.xlsx (Workbook OBE K2025)
├── Notulensi Rapat VMTS & Kurikulum Program Studi SIST 090626.pdf (Notulensi — BUKAN ground truth MK)
├── [IA - UPPS] ... INSTRUMEN PEMENUHAN SYARAT MINIMUM AKREDITASI ... .pdf (Instrumen akreditasi)
└── obe_pdf_extract/ (Hasil ekstraksi Modul OBE 2025: 56/56 kode cocok, 0 konflik SKS)
```

---

## Current State & Next Steps

**Status Saat Ini:** 
- **Fase Makro OBE:** VMTS ↔ 3 PEO ↔ 4 PL ↔ 14 CPL ↔ 19 BoK IS2020 & 14/27 BoK IT2017 ↔ Struktur 8 Semester (146 SKS paket ditempuh / 182 SKS portofolio ditawarkan) ↔ 3 Peminatan Seimbang (@ 18 SKS) telah **100% tuntas dan terverifikasi di Dokumen 001–006**.
- **Fase Mikro OBE & Silabus 3-Tabel:** Formulasi Identitas MK, CPMK berbasis ABCD & Taksonomi Bloom (C2–C6), serta Matriks 16 Pertemuan dengan Skema 4x Asesmen (Tugas 1 [20%], UTS [25-30%], Tugas 2 [20-25%], UAS [30%]) untuk **seluruh 67 MK portofolio** telah **100% tuntas di Dokumen 007 (361 KB)**.
- **Fase Asesmen, Tugas Akhir, & Penjaminan Mutu:** Sistem Asesmen OBE (IKU 7 $\ge 50\%$, Formula Ketercapaian CPL, 4 Rubrik Analitik Master), Pedoman Capstone & 4 Opsi TA Non-Skripsi, serta Instrumen Tracer Study PEO telah **100% tuntas di Dokumen 008, 009, dan 010**.
- **Fase Pertukaran Struktur Semester 6–7 & Standardisasi Bilingual:** Pertukaran 8 SKS mata kuliah tingkat akhir antara Semester 6 (`FST-610`, `FST-612`, `FST-613`) dan Semester 7 (`STI-726`, `STI-727`, `STA/B/C-602`) telah **100% tuntas dan tersinkronisasi di 23 dokumen markdown kurikulum**. Menghilangkan cognitive overload di Semester 7, menyatukan Metodologi Penelitian dengan Pra-Skripsi di Semester 6, dan menyelaraskan 4 MK peminatan di Semester 7. Seluruh tabel sebaran MK Dokumen 005 distandarisasi ke format dwibahasa (*bilingual*) Indonesia–English via `_tools/apply_005_id_en.py`. Seluruh workbook Excel diekspor ulang (`MASTER_KURIKULUM_OBE_SISTEKIN_2026.xlsx`, `011...xlsx`), dan lulus uji QA terprogram 100% selaras pada Dok 005 dan PDF SIAKAD K2025 (Dokumen 050).
- **Fase Audit Kritis & Akselerasi:** Kunci konsensus `STI-103 Arsitektur & Organisasi Sistem TI` dan `STI-204 Matematika Diskrit dan Logika`, Solusi Mitigasi (013), Simulasi Fast-Track 7 Semester (015), Pipeline AI (016), dan Audit Forensik Zero Redundancy & Zero Gap (017) telah **100% tuntas dan terverifikasi di Dokumen 012–017**.
- **Fase Naskah Buku Kurikulum Final:** Naskah utuh komprehensif Bab 1 s.d. Bab 8 (`BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`, 445 KB) telah selesai dan 100% selaras dengan seluruh dokumen pendukung.
- **Fase Restrukturisasi Kode MK Core STI Kontinu:** Penomoran 28 MK Core STI telah **100% tuntas distandarisasi ke skema berkesinambungan (`STI-101` s.d. `STI-728`)** di seluruh 23 berkas markdown dan skrip automasi Python (1.348 titik penggantian atomik). Menyembuhkan anomali lompatan nomor 406 dan 502, menyelaraskan konvensi dengan MKWU (`MKU-101..508`) dan SIAKAD UWG. Terverifikasi lulus *Zero Discrepancy* dan 11/11 audit ground truth SIAKAD (Dokumen 027 & 028).
- **Fase Restrukturisasi Kode MK Peminatan (STA, STB, STC):** Penomoran 18 MK Pilihan Peminatan telah **100% tuntas distandarisasi dari format 2-digit (`STA-01..06`, `STB-01..06`, `STC-01..06`) menjadi format 3-digit berbasis semester dengan reset ke `01` pada setiap semester (`STA/STB/STC-501`, `601..602`, `701..703`)** di seluruh 22 berkas markdown dan 8 skrip automasi Python (660 titik penggantian atomik). Menghilangkan anomali kode tidak bersemester, menyelaraskan format dengan MKWU/FSTI/Core STI, serta menyiapkan jalur ekspansi pilihan Dokumen 025 (`502..503`, `603..604`, `704..705`). Terverifikasi lulus *Zero Discrepancy* (100% perfect alignment) dan 11/11 audit ground truth SIAKAD (Dokumen 035 & 036).
- **Fase Boundary of Topics & Matriks Anti-Overlap Kurikulum:** Instrumen audit kurikuler dan pengendali mutu kurikulum telah **100% tuntas di Dokumen 037**, menetapkan 3 pagar pembatas (*In-Scope, Out-of-Scope, Handoff Anchor*), memetakan 21 BoK IS2020 & 15 BoK IT2017 ke 14 CPL, membedah secara mendalam **8 Klaster Kritis Rawan Overlap**, menganalisis **seluruh 18 MK Pilihan Peminatan (STA, STB, STC)** dengan formulasi CPMK ABCD & Sub-CPMK kunci, menetapkan **Peta Boundary Baseline 8 pasang/trio MK Core STI**, serta memformalkan **5 Aturan Emas Bebas Overlap (*5 Golden Rules*)** bagi dosen pengampu dan Gugus Penjaminan Mutu (GPM).
- **Fase Ekivalensi & Transisi Kurikulum:** Matriks ekivalensi 56 MK Kurikulum 2025 ke Kurikulum 2026 telah **100% tuntas di Dokumen 024**, mencakup 5 kategori penyetaraan (E1 Penuh 34 MK, E2 Bersyarat 11 MK, E3 Gabungan 8 MK, E4 Pecah 1 MK, E5 Tanpa Padanan 2 MK), 4 klaster peleburan MK (G-1 s.d. G-4, efisiensi −7 SKS), peringatan kolisi kode `STI-102`/`STI-103`, 18 MK baru K2026 (5 MK wajib / 14 SKS + 13 MK elektif), simulasi pengakuan SKS per jalur peminatan (P1/P2 = 120 SKS diakui, P3 = 117 SKS), serta tabel siap impor `mk_ekivalensi` SIAKAD (57 baris konversi).
- **Fase Verifikasi Ground Truth K2025:** Dokumen 024 telah **diaudit terprogram terhadap PDF Laporan SIAKAD** (`_tools/verify_k2025_ground_truth.py`, 11 kelompok uji) dan **LULUS 17 butir verifikasi**: 56 MK / 146 SKS, sebaran 8 semester, nomor urut & nama & SKS tiap baris identik PDF (0 ketidakcocokan), 0 baris salah seksi semester, Zero Orphan, 0 kode fiktif, neraca E1–E5 = 146 SKS, 49 kode target K2026 valid, simulasi SKS 120/120/117 terkonfirmasi, semester MK elektif presisi, neraca rekognisi arah balik 114 diakui / 14 defisit SKS, portofolio 67 MK = 49 direkognisi + 18 baru, serta 2/2 kasus klaim ganda tuntas.
- **Fase Penyamaan Versi & Rekognisi Dua Arah:** Dokumen 024 kini memuat **Bagian 3A Matriks Rekognisi Arah Balik (K2026 ← K2025)** — 8 tabel per semester yang menyatakan untuk setiap MK Kurikulum 2026: SKS, kategori ekivalensi, MK asal K2025, dan tindakan akademik (alih nilai langsung / uji penyetaraan / wajib tempuh). Neraca paket wajib: **114 dari 128 SKS diakui (89,1%), defisit 14 SKS pada 5 MK baru**. Semester 4, 5, dan 8 terekognisi 100%; titik kritis penyisipan ada di Sem 1 (`STI-103`) dan Sem 3 (`STI-312`) karena keduanya prasyarat berantai. Ditambahkan pula peta navigasi dokumen per peran pengguna, aturan klaim ganda berjenjang 2 tingkat (menuntaskan ambiguitas `STI-422` vs `STI-742` yang keduanya E2), dan Bagian 9.3 konsistensi dua arah matriks.
- **Fase Diseminasi untuk Pembaca Non-Teknis:** Dokumen 024 diterbitkan ulang dalam format ramah-awam via `_tools/export_024_awam.py`, menerjemahkan kode kategori E1–E5/B menjadi kalimat tindakan lugas (Diakui penuh / Diakui bersyarat / Digabung / Dipecah / Tidak ada padanan / Kalah prioritas / Wajib ditempuh) dengan pewarnaan konsisten. Keluaran: **XLSX 8 sheet** (Baca Ini Dulu, 2 arah konversi, neraca per semester, MK wajib baru, MK peminatan, klaster peleburan, sumber data — berheader beku & berfilter) dan **DOCX 9 tabel lanskap** siap cetak untuk rapat prodi dan sosialisasi mahasiswa. Kedua berkas dibangkitkan langsung dari PDF SIAKAD + Dok 005/007/024, bukan disalin manual.
- **Fase Matriks Terpadu CPL, CPMK, BoK, & Boundary Guardrails:** Matriks terintegrasi operasional per semester telah **100% tuntas di Dokumen 043** (`043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md`, 348 KB; varian lembar kerja detail: `043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md`), merinci **28 MK Core STI (Semester 1 s.d. 7)** dan **18 MK Peminatan (Semester 5 s.d. 7)** secara komprehensif. Setiap MK dilengkapi pemetaan CPL, formulasi lengkap CPMK berbasis format baku ABCD (Audience, Behavior, Condition, Degree) dan level Taksonomi Bloom (C2-C6), rujukan Bahan Kajian BoK APTIKOM SI (IS2020) dan TI (IT2017/CC2020), serta 3 lapisan Boundary Guardrails (*In-Scope, Out-of-Scope, Handoff Anchor*) untuk menjamin *zero curricular overlap*.
- **Fase Penetapan Definitif STA-601 Big Data Engineering:** Evaluasi kritis atas relevansi matematika komputasi dan kebutuhan industri melahirkan keputusan definitif penggantian *Computational Methods and Numerics* menjadi **`STA-601 Rekayasa Big Data dan Komputasi Terdistribusi` (*Big Data Engineering & Distributed Systems*)** berbobot **3 SKS (+Praktikum)** pada Semester 6 Peminatan P1 (prasyarat `FST-207` + `STI-415`, CPL `P2`/`KK2`, BoK `BK-IS02` primer & `BK-IS18` sekunder; Apache Spark, PySpark, Data Lakehouse Delta Lake, Apache Kafka, Spark MLlib). Menyembuhkan anomali *curricular orphan gap* (janji CPL `KK2.1` PySpark yang sempat dilarang di `STI-520`). Opsi alternatif Riset Operasi dialokasikan ke pool pilihan bebas cross-track 2027 (`STA-603` di Dok 025). Tuntas terverifikasi 100% selaras di seluruh 14 dokumen ekosistem kurikulum tanpa mengubah neraca paket kelulusan (Dokumen 047, 048, 049).
- **Fase Analisis Template RPS Generator & Pilot RPS:** Audit desain layout, geometri halaman, hirarki tabel, serta penyusunan **Kamus Tag Placeholder** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx` / `-SWI.pdf`) telah tuntas di **Dokumen 052**, menetapkan konvensi 2 format placeholder yang **keduanya merupakan placeholder template**: **`{{tag}}` = placeholder nilai tunggal** (18 tag unik, mis. `{{namamk}}`, `{{kodemk}}`) dan **`[tag]` = placeholder blok isi** yang dapat berisi **paragraf, tabel, list, atau konten yang lebih kompleks daripada `{{tag}}`** (25 tag unik, mis. `[cpl]`, `[tabelkolerasi]`, `[rubriktugas1]`). Pilot RPS pertama telah dibangkitkan untuk **`STI-416 Web Back End Development`** (markdown + DOCX, versi V2 simplified), lengkap dengan laporan pengembangan (`LAPORAN_PENGEMBANGAN_RPS_STI416_V2.md`) dan audit verifikasi keselarasan terhadap Dok 007 (`VERIFIKASI_KESELARASAN_RPS_STI416_V2_DENGAN_DOK_007.md`).
- **Fase Pembangkitan Paket Perangkat Ajar OBE & Reorganisasi ke `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`:** Paket perangkat ajar OBE 5-dokumen per mata kuliah (`_1_RPS`, `_2_SAP`, `_3_OUTLINE_MODUL`, `_4_RENCANA_EVALUASI_ASESMEN`, `_5_RUBRIK_PENILAIAN`) untuk **Tahap 1–4 (Semester 1 s.d. Semester 4: `055 STI-101` s.d. `072 STI-418`, 18 MK = 90 berkas `.md`)** telah tuntas disusun, diperkaya mendalam pada `055`–`059`, dan **direorganisasi ke dalam folder khusus `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`** lengkap dengan manifest `KURIKULUM2026_REVISI/PERANGKAT_AJAR/README.md`. Seluruh generator bahan ajar lainnya (baik untuk ekspansi mendalam `060`–`072`, pengayaan Tahap 5–6 `073`–`085`, maupun pengayaan Tahap 7 `086`–`100` yang telah tersedia) **wajib langsung melanjutkan di dalam folder `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`**.

**Temuan Terbuka (BELUM ditindaklanjuti — menunggu persetujuan Tim Kurikulum):**
- **Dokumen 026** mengaudit 2 MK berkategori E5 (`STI-423` Game Design & Gamifikasi Sosial, `STI-638` Intelligent Signal Processing) dan menemukan **3 klaim penyerapan pada Dok 024 tidak terbukti**: gamifikasi diklaim terserap di `STC-501`/`STC-701` (hasil pemindaian: nol kemunculan; jangkar sebenarnya `STC-602` Pekan 9), sinyal diklaim terserap di `STA-703` (nol kemunculan), dan sitasi "Dok. 016" tidak dapat dilacak (kedua MK tidak pernah dibahas di Dok 016/017).
- **Uji ambang E2** (overlap 60–85%) atas 5 kandidat MK pengganti: seluruhnya gagal, overlap tertinggi hanya **6,2%** (`STC-602`). Karena itu **status E5 dipertahankan** — memaksakan ke E2 akan mengubah angka konsensus (E5 2→0 MK, simulasi 120/120/117 → 123/120/120 SKS) tanpa dasar substantif, dan pengakuannya tidak setara antar jalur.
- **Penghapusan kedua MK itu sendiri SAH**: 14 CPL K2026 tidak menyebut gamifikasi/sinyal/multimedia sama sekali (K2025 `CPL04` menyebut eksplisit), dan di K2025 keduanya bukan pengampu tunggal (CPL-nya diampu 17 dan 31 MK lain).
- **Angka konsensus Dok 024 TIDAK berubah**: E1 34 / E2 11 / E3 8 / E4 1 / **E5 2** MK; simulasi P1 = P2 = 120 SKS, P3 = 117 SKS. Rumusan catatan pengganti tersedia di Dok 026 Bagian 6.1 dan bersifat perbaikan redaksi saja.
- **Placeholder tanda tangan RPS pilot STI-416 belum terisi:** `RPS_STI-416_Web_Back_End_Development_V2_SIMPLIFIED.md` masih memuat `[Nama Ketua Tim Kurikulum]`, `[Nama Ketua Prodi]`, `[Nama Kepala UPM FSTI]`, dan `[Nama Dosen Koordinator MK]` pada blok tanda tangan — perlu nama pejabat sebelum dokumen diedarkan.

---

*File ini berfungsi sebagai "memory/soul" untuk semua agent yang bekerja di folder ini.*
- **Tahap 5 selesai:** Semester 5 `073`–`080` tersedia 40 berkas (8 MK × 5). Tahap 6 kini juga tersedia (lihat status di bawah). Validasi dosen/koordinator masih diperlukan atas catatan rekonsiliasi antardokumen sumber dan rencana pembelajaran.

- **Tahap 6 selesai:** Semester 6 `081`–`085` tersedia 25 berkas (2 MK Core STI + 3 MK peminatan × 5). Tahap 7 `086`–`100` sudah tersedia; perlu audit substantif dan validasi koordinator. Kode Core Semester 6 pada Dok 043/004 masih memakai kode lama; cocokkan berdasarkan judul dan ikuti Dok 005/051. Catatan rekonsiliasi tetap membutuhkan validasi koordinator.

- **Status Tahap 7:** Paket `086`–`100` telah tersedia. Paket peminatan `089`–`100` direkonsiliasi dengan Dok 003/004/005/007/043; pengayaan dan validasi pengampu tetap diperlukan. Paket Core `086`–`088` juga perlu audit substantif. Verifier identitas Dok 005 bukan audit kualitas isi.

- **Revisi STI-311 (rancangan, belum disahkan):** Dok 005 tetap menentukan identitas; Dok 043 induk/per semester, ekstraksi, 007, 037 dan paket `PERANGKAT_AJAR/065_1`–`065_5` telah diselaraskan pada HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap/Tailwind dasar dan JavaScript dasar, tanpa React/SPA, Fetch/asinkron atau API. Jangan gunakan RPS pilot lama tanpa rekonsiliasi. Lihat `KURIKULUM2026_REVISI/LAPORAN_AUDIT_DAMPAK_STI-311.md` untuk MK hilir dan pekerjaan non-Markdown; validasi/pengesahan prodi masih terbuka.
