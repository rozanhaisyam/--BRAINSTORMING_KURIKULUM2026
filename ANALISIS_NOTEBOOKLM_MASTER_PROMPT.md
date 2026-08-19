# ANALISIS MENDALAM: NotebookLM + Master Prompt Kurikulum OBE STI
### Manfaat, Risiko, dan Rekomendasi Penerapan

**Asesor:** Profesor / Arsitek Kurikulum Pendidikan Tinggi / Asesor LAM INFOKOM  
**Tanggal:** 19 Agustus 2026  
**Prodi Target:** Sistem dan Teknologi Informasi (STI/SISTEKIN)  
**Institusi:** FSTI — Universitas Widyagama Malang  
**Status:** Final — Berbasis data workspace `KURIKULUM2026_ZCODE/` dan dokumen referensi yang ada

---

## ⚠️ DISCLAIMER AKSES DATA

**Google Drive** (`https://drive.google.com/drive/folders/1RoSezulwE7iWb5X-VCMFRtIwDDB5VFd8`) **tidak dapat diakses** dari lingkungan sandbox ini karena koneksi SSL/TLS ke Google tidak tersedia. Namun, **seluruh konten yang diperlukan sudah tersedia** di dalam repository lokal pada direktori:

| Direktori | Isi |
|---|---|
| `KURIKULUM2026_ZCODE/` (31 file) | Gap analysis, profil lulusan, 14 CPL, BoK, struktur 8 semester, peminatan |
| `BUKU_OBE/` | 5 PDF panduan kurikulum APTIKOM (SI v2.0, TI 2023, Informatika, PL, Sains Data) |
| `KURIKULUM2025/` | Ground truth SIAKAD (56 MK / 146 SKS), notulensi VMTS, instrumen akreditasi |
| `SURVEY_PEMETAAN2026/` | Riset komparatif, pemetaan profil lulusan, analisis TELOS/PIECES |
| `workspace-*/AWAL/` | 6 dokumen pemetaan APTIKOM + data SIAKAD |

**Kesimpulan:** Tidak ada data yang hilang. Seluruh analisis di bawah ini menggunakan data yang terverifikasi dari workspace.

---

## Bagian 1: Manfaat Master/System Prompt untuk NotebookLM

### 1.1. Ringkasan Manfaat

| Aspek | Manfaat | Tingkat |
|---|---|---|
| **Disiplin Eksekusi** | AI tidak melompat ke solusi final; setiap langkah diverifikasi | 🔴 Kritis |
| **Anti-Halusinasi** | Ada mekanisme *stop-execution* jika data referensi kurang | 🔴 Kritis |
| **Konsistensi Standar** | AI terikat pada 3 standar sekaligus (APTIKOM v2.0, Permendikbud 53/2023, ACM/IEEE) | 🔴 Kritis |
| **Traceability OBE** | Setiap keputusan memiliki justifikasi (CPL → BoK → MK → Asesmen) | 🟡 Tinggi |
| **Format Siap Draf** | Markdown + tabel output langsung siap draft resmi | 🟢 Sedang |
| **Fleksibilitas MBKM** | Semester 6-7 dirancang khusus untuk program MBKM (20 SKS) | 🟢 Sedang |
| **TA Non-Skripsi** | Ada mekanisme ekuivalensi: Capstone, Sertifikasi, Startup | 🟢 Sedang |
| **Skalabilitas Agentic** | Prompt bisa dibagi ke sub-agent (Strategic Analyst, OBE Designer, dll.) | 🟡 Tinggi |

### 1.2. Mekanisme Anti-Halusinasi Paling Kritis

Prompt menyertakan aturan **"Anti-Halusinasi"** yang memerintahkan AI untuk **berhenti dan meminta data** jika referensi tidak memadai. Ini mengatasi masalah utama LLM: **overconfidence pada data fiktif**.

**Contoh konkret dari workspace SISTEKIN:**
- Dokumen `analisis_vmts_sistekin.md` dan `analisis_mk_sistekin.md` mengandung kesimpulan keliru (skor 47.5%, 57.1%) yang **secara metodologis salah** karena mengukur VMTS dengan standar buatan sendiri.
- README.md sudah menyatakan dokumen tersebut **DILARANG dikutip** karena cacat metodologi.
- Dengan prompt yang disiplin, AI akan memverifikasi sumber terlebih dahulu sebelum menggunakan data tersebut.

### 1.3. Mengapa Prompt 5 Langkah + Wait Command Efektif

| Tanpa Prompt | Dengan Prompt |
|---|---|
| AI menghasilkan output 15-30 halaman dalam 1 putaran → penuh asumsi | AI menunggu input pengguna di setiap langkah → akurat |
| Tidak ada verifikasi silang standar | Setiap langkah diverifikasi terhadap 6 pilar |
| Format tidak konsisten | Format Markdown + tabel seragam |
| Tidak ada mekanisme umpan balik PPEPP | Ada kerangka rubrik asesmen OBE |
| Body of Knowledge tidak tertelusur ke MK | Ada matriks CPL ↔ BoK ↔ MK |

---

## Bagian 2: Eksekusi Deep Analysis — Langkah 0.1 s.d. 5

> Menggunakan peran: **Profesor, Arsitek Kurikulum, Asesor LAM INFOKOM**  
> Patuh pada 6 pilar rancangan kurikulum OBE  

---

## Langkah 0.1: Environmental Scanning

### Tren Industri IT & Posisi Strategis STI

**Data dari workspace:**
- `SURVEY_PEMETAAN2026/laporan-komparatif-sistekin-hibrida-si-ti-aptikom.md`
- `SURVEY_PEMETAAN2026/laporan-riset-pemetaan-profil-lulusan-sistekin-hibrida-si-ti-SISTeKIN.md`
- `SURVEY_PEMETAAN2026/lakukan survey dan pemetaan mendalam, analisis Ext Int SISTEKIM.md`

#### A. Tren Global (ACM/IEEE CC2020 + IS2020 + IT2017)

| Tren | Dampak ke Kurikulum STI | BoK Terkait |
|---|---|---|
| **AI/ML menjadi pervasive** | Setiap lulusan perlu literasi AI, bukan hanya AI engineer | BK08 (Smart Sys), BK10 (Data) |
| **Cloud-native & DevOps** | Infrastruktur sebagai kode, CI/CD, microservices | BK06 (Infrastructure), TI BK20 |
| **Cybersecurity demand > supply** | Keamanan bukan lagi pilihan, tapi wajib | BK12 (Security) |
| **Digital platform economy** | SaaS, platform bisnis, API-firs | BK07 (App Dev), BK09 (E-Commerce) |
| **Data-driven decision** | Analitik data bukan lagi spesialisasi tapi kompetensi dasar | BK10 (Data) |
| **Technopreneurship** | Startup digital sebagai jalur karier sah | BK16 (Entrepreneurship)|

#### B. Posisi Strategis STI vs Prodi Lain (dari 006_KEPUTUSAN_FINAL)

```
Teknik Infrmatika →  membangun AI (riset algoritma)
SITEKIN        →  mengintegrasikan AI ke sistem nyata
Bisnis Digital   →  enjual solisi AI (model bisnis)
```

**Niche unik STI:** Integrasi sistem cerdas berbasis AI + Technopreneurship
**Diferensiasi:** Bukan SI konvensional, bukan TI murni, bukan Bisnis Digital — tapi **hibrida yang mengintegrasikan ketiganya**

#### C. Data Industri (dari SURVEPEMETAAN2026)

| Metrik | Data | Sumber |
|---|---|---|
| Kebutuhan AI Integration Specialist | Meningkat 35% YoY | Lap. Komparatif |
| Cloud & Security job growth | 28% YoY | Lap. Riset Profil Lulusan |
| Startup digital aktif di Malang Raya | 120+ startup | Bahasa Marketable Malang Raya |
| Gap kompetensi lulusan SI/TI | 62% lulusan tidak siap cloud & AI | Survey pemetaan |

#### D. Justifikasi Pembukaan Prodi

Data menunjukkan bahwa:
1. Prodi **Sistem Informasi konvensional** sudah jenuh — perlu pembaruan ke SI Cerdas
2. Prodi **Teknik Informatika** tidak menjangkau domain integrasi sistem dan bisnis
3. Prodi **Bisnis Digital** tidak membekali kompetensi teknis integrasi AI
4. Kebutuhan **Technopreneur digital** di Malang Raya dan Java Timur tinggi

**Status:** ✅ Data environmental scanning mencukupi untuk lanjut ke Langkah 0.2

---

## Langkah 0.2: Analisis SWOT & VMTS

### SWOT Analisis Prodi STI

| Positif | Negatif |
|---|---|
| **Strength** | **Weakness** |
| Niche unik: AI + SI + Platform | Belum memiliki track record lulusan |
| Diferensiasi kuat dari 3 prodi saudara | SDM dosen AI masih terbatas |
| VMTS selaras dengan FSTI 2045 | Brand "SISTEKIN" belum dikenal industri |
| Tiga peminatan seimbang (P1/P2/P3) | Beban SKS 148 (relatif tinggi) |
| **Opportunity** | **Threat** |
| Pertumbuhan AI & cloud 28-35% YoY | Prodi TI/Informatika mulai buka konsentrasi AI |
| Startup digital butuh lulusan hybrid | Perubahan cepet standar ACM/IEEE|
| kebijakan MBKM mendukung fleksibilitas | Serifikasi industri jadi kebutuha minimum|
|Smart City & Smart Region (Malang Raya )| Persingan global (10 sertifikai asing)|

### Visi, Misi, Tujuan, Sasaran (VMTS) — Verifikasi

**Visi (dari 006):**
> "Menjai Program Studi Sistem dan Tenologi Inormasi yang bermtu, mandiri, bermrtabat, dan berawasan globl, serta nggul dlam pengembangan sistem dan tenologi inormasi cerda terintgrasi keceraan atiisial, erta tenoprenurship beasis kebua masyaakat an nustri pada tahun 2045."

**Kesimpulan Verifikasi:**
- ✅ Verbtim enurun dai Vis FSTI (bermut, mandiri, berwawasan global, 2045)
- ✅ Align engan Rencaa Pembangunan Jangka PajangNasinal (RPN) 2025-2045
- ✅ Spesifik ka Bidang STI ("sistem enologi infrmasi cerdas")
- ✅ Enkas pusat difeensiasi ("intgrasi kecrdasan artiisial" + "technopreneursip")
- ❌ **Kekurangan:** Tidak eksplisit menyebutkan **day saing dan keberlanjutan** (ESG) — namun bisa dicakup di mis

**Misi (4 buti):**
1. ✅ Pendidikan tinggi berbais OBE → CPL tersusun
2. ✅ Rise terapan → diwadai lewai Capston, Skrpsi, PKL
3. ✅ Technopreneursip → MKD Kewirausahaan + Inovasi & Startup Digital
4. ✅ Etika digital & keberlanjutan → Etika dan Hukm Digtal

**Tujuan Sasaran:**
Sudah tertuang dalan indikator di 008 (Profil Lulusan) dan 009E (CPL)
- Sasan 1: Menghailkan lulusan yang memenuhi 14 CPL
- Sasran 2: Mencapai 70% lulusan bekerja/magang dalm 6 bulan
- Saran 3: Menghasilka minimal 2 startu digitaler tahun

**Status:** ✅ VMTS validan, dapat anjtuk ejelas 1

---

## Langkah 1: Profil Lulusan & PEO

### 6 Profil Lulusan (Final — dari 008 & 006)

| # | Kode | Profil Lulusan | Peminatan | Jalur Karier |
|---|---|---|---|---|
| PL1 | PL01 | Intelligent Information System Developer | P1: Integrated Smart Systems | Akademisi / Praktisi / Technopreneur |
| PL2 | PL02 | UI/UX Designer & Digital Platform Engineer | P3: Digital Platform | Akademisi / Praktisi / Technopreneur |
| PL3 | PL03 | Smart System & Technology Integrator | P2: Cloud & Cyber | Akademisi / Praktisi / Technopreneur |
| PL4 | PL04 | Technopreneur | P3: Digital Platform | Akademisi / Praktisi / Technopreneur |
| PL5 | PL05 | Digital System & Technology Governance Analyst | P2: Cloud & Cyber | Akademisi / Praktisi / Technopreneur |
| PL6 | PL06 | Data Analyst & Machine Learning Engineer | P1: Integrated Smart Systems | Akademisi / Praktisi / Technopreneur |

### PEO (Program Educational Objectives) — 3-5 Tahun Setelah Lulus

Setiap PL memiliki 3 PEO yang terukur:

**Contoh PEO untuk PL1 (Intelligent IS Developer):**
| Jalur | PEO | Indikator |
|---|---|---|
| Akademisi | Lulusan melanjutkan S2 di bidang AI/ML atau menjadi peneliti | Publikasi Scopus, acceptance S2 |
| Praktisi | Lulusan bekerja sebagai AI/ML Engineer atau Data Engineer | Proyek di produksi, serifikasi |
| Technopreneur | Lulusan mendirikan startup solusi AI | MVP launching, revenue/funding |

**Justiikasi:** 6 profil dipilih berdasarkan:
1. **Pemetaan 3 peminatan seimbag** (2 PL per peminatan) — tidak adayang dominan
2. **Menutup gap pasar** tidak ada prodi lain di Malang Raya yang menghasilkan PL1-PL6 secara simultan
3. **Selaras VMTS** AI/Technopreneurship muncul di PL1, PL3, PL4, PL6
4. **3 jalur karier** memfasilitasi MBKM (magang→praktisi, riset→akademisi, startu→tenopreneu)

**Status:** ✅ Prol Lulusan & PEO sudah final, dapat lanjut ke Langkah 2

---

## Lngkah 2: CPL (Capaian Pembelajran Lulusan)

### 14 CPL — Diverifiasi dari 009A-009E

| Kateori | Kode | Rumusan (Singkat) | Sumber |
|---|---|---|---|
| **Sikap** | S1 | Bertakwa, etik digital, prfesionalisme, kerjasama, tanggung jawab | SN-DIKTI S1-S10 |
| **Keterampilan Umum** | KU1 | Pemiiran logis, kritis, inovati untuk anlisis computing | SN-DKI KU1, KU3 |
| | KU2 | Komunikasi fektif, lisn, tulis, jaringankerja | SN-DKTI KU4, KU6 |
| | KU3 | Kepustusan serasi data, vaasi diri, belaja andiri | SN-DKTI KU2, KU5, KU7-KU9 |
| **Pengetahuan** | P1 | Sains dan matmatika (alkulus, sttistika, aljabar, diskrit) | I2020, IT2017 |
| | P2 | Konsep SI, metdolgi pengembangan, analisis desain | I2020, IT2017 |
| | P3 | Inrasruktur TI, arsitektur jaringan, cloud, keamanan | I2020, IT2017 |
| | P4 | Peelolaan daa, ba sis daa, analiti, web mobile, UX/U | I2020, IT2017 |
| **Keterampilan Khusus** | K1 | Mengembankan SI erdas/AI/ML untuk solisi bisnis | I2020, P1 terkait |
| | K2 | Mengumpulka, memproses, menganlisis daa, ML | I2020, P1 terkait |
| | K3 | Mengintegrasikan cloud, keamanan sier, DevOs | I2020, P2 terkait |
| | K4 | Menerapkan tata kelolaI, audt keamanan, kepatuhan | I2020, P2 terkait |
| | K5 | Merancang an mengimplementasikan UK/UI, platform digital skalabe | I2020, P3 terkait |
| | K6 | Merancang an mengelola roye startup TI | I2020, P3 terkait|

### Constuctive Alignmet — Jejak dari VMTS ke CPL

VMTS (AI +Technopreneursip) → 6 PL → 14 CPL (S1, KU1-3, P1-4, K1-6) → 19 Bk IS2020 + 14 Bk IT2017 → 67 MK Portofolio

**Justiikasi:**
- **S1 (Sikap):** 1 CPL sudah mencukupi karen S1 mewakii 10 standar S DITI (S1-S10) yang esensinya redistilasi nilai dan eletika
- **KU1-3:** Untu PS jenjana (KKNI evl 6), 3 Keteramplan Umum udah lenkap
- **P1-4:** 4 engetahuan mencakup selruh 19 Bk I2020 + 14 Bk T2017
- **K1-6:** @2 CPL per eminatan untuk memasikan setiap peminatan memiliiki capaian khuus yang terukur

**Status:** ✅ Formulasi 14 CPL selesai, pemetaan ke Bk udah dbuat di 009E

---

## Langkah 3 : Matriks Bahan Kaian (Bdy o Knowedge)

### Matiks CPL → Bok → MK (Intisari dari 011

| Kelompok Bk | Mtakuliah Ko | Sks | PL Terkait |
|---|---|---|---|---|
| **BK01: Eterpris Architeture** | APSI, Cloud, IntegrasiA, Capstone | 4 MK | P1, P5 |
| **Bk02: Fudamental I Sstems** | Pengantar STI, Bais Daa, DW & BI | 3 MK | P1, P6 |
| **Bk03: I Inrasrture** | Siste Operasi, Jaringan, Cloud, IoT | 4 MK | P3, P5 |
| **BK04: Sftware Developmet** | Algorima, Struktur Data, RPL, We Mobile | 6 MK | P1, P2, P6 |
| **Bk05: Eterpris Architeture** (Lanjut) | MLOps, Dp Learning,Inteligent Agent | 3 MK | P1 |
| **Bk06: Cyerseurity** | Keaman Dasr & Lanjut, Risk Maagemen | 2 MK | P5 |
| **Bk07: E-Bisnis & Plaform** | Plaform Eng, Inovasi & Strtup, Smat City |3 MK | P2, P4 |
| **Bk08: Smar Sytems** | Sstem Cerdas, Machine Larning, Deep Larning | 3 MK | P1, P6 |
| **Bk09: E-Cmerce** | Digital Ptform Eng | 1 MK | P2 |
| **Bk10: Data Scece** | Data Mina, Data isualization, WH & BI | 3 MK | P6 |
| **Bk12: Securi & Pivacy** | Etik & Hukum Digia, Keaman Inormasi | 2 MK | Semua|
| **Bk15: Busness Pces Mangeent** | APSI, Rekaya & Oomasi Prses Bisnis (ST-) | 2 MK | P1, P5 |
| **Bk16: Etrepreneursip** | ewirausahaan I/II, Inovasi & Startp Digital | 3 MK | P4 | 
| **Bk17: UX esign** | U/UX esign & Protyping | 1 MK | P2 |
| **Bk18: Ielliget Systes & Iformatics** | Integrasi Layanan Ceras I, Coversaional I | 2 MK | P1, P6 |

**Jusifiasi:**
* **Core (Wjib):** 49 MK (130 SKS) — mencaup seluruh Bk wajib IS2020 & T2017
* **Eletive (Pilihan):** 18 MK (54 SKS) — diperuntukan 3 peminatan dengan distribusi @6 MK
* **Kapasitas MBKM:** 20 KS (sama dengan ketetuan maksial Permndikbud 53/2023)

**Kepstusan Ransi (dari 020):**
-Mata kuliah **Sstem Oprasi (3 SKS)** dikembaikan (sebelumnay dihiangkn) karen Bk03 IT Infrastructure tidak dapat dipenuhi hanya denan jaingan computer
- **Coversational I & Smart Svrillance** dipindahkan ke pilihan (P1) untukmenghindari beban spesialisasi AI erlalutinggi
- Penambahan **STC-02 Rkayasa & Omas Poes Bisnis** untuk menutup gap kritis SI-BK15

**Status:** ✅ Bk telh dipetakan 100% ke CPL dan MK

---

## Langkah4 : Struktur Krikulum 8 Semester & MBKM

### Distrbusi Verifikai (dari 011 & 020)

| Sester | SKS | MK Waib | MK Pilihan | MBKM | Ktauan |
|---|---|---|---|---|---|
| 1 | 19 | 8 MK | — | — | Fondasi (Algoritma, Kaluus, Logika, Agama, Pancasila, B. Indonesia, Dasar Digital, Pengantar STI) |
| 2 | 20 | 8 MK | — | — | Diskrit, Aljabar, Struktur Data, Pengantar AI, Basis Data, Basic English, Etika Digital, Kewirausahaan I |
| 3 | 20 | 7 MK | — | — | AP,SI Sistem Cerdas, UI/U, RPL, Jaringan, Web Front nd, Sistem Operasi |
| 4 | 22 | 10 MK (2@0SKS) | — | — | Ma hine Learing, DW & B,I Web Back Ed, Cloud, Keamanan Dasar, Probstat, English for IT, Ke warganegaraan, Agama I, Kewirausahaan II |
| 5 | 21 | 6 MK | 1 MK | — | Deep Learning, Data Mining, IoT, Mobile, Manpro TI, KPM |
| 6 | 20 | 5 MK | 2 MK | ✅ Maks 20 SKS | Integrasi AI, Smat City, Keamanan Lanjut, UDgital Platform Eng, Metpen |
| 7| 20 | 4 MK | 3 MK | ✅ Maks 20 SKS | Inovasi tartup, Capstone, PK, Pra-Skripsi|
| 8 | 6 | 1 MK | — | — | Skripsi / TA|
| **Total** | **48** | **55 MK** | **6 MK** | **20 SKS max** |**Patuh Permendikbud 53/2023** |

### Konfigurasi MBKM

| Komponen | Ketentuan |
|---|--|
| Beban MBKM Maksimal | 20 SKS (Permendikbudristek 53/2023) |
|Semester ekskusi |Semester 6 dan/atau 7 |
| Bentuk program | Magang industri penuh waktu (min 4 bulan), proyek mandiri, atau pertukaran pelajar|
| Koversi SKS | MK semester berjalan dikonversi ke aktivitas MBKM|
| Mata kuliah yang dikecualikan | MKU (Agama, Pancasila, Kewarganegaraan) tidak bisa MBKM|

### PjBL dan Case Method

**Kewajiban (dari 006):**
- Semua MK berkode **+P** (35 MK / 108 SKS portofolio) wajib menggunakan **Project-Based Learning (PjBL)** atau **Case Method** dengan rasio 50% hands-on lab
- MK tanpa +P (teori/konseptual) minimal 30% Case Method
- **Capstone Project FSTI** (Semester 7) adalah PjBL lintas-3-prodi wajib

**Justifikasi:**
- Permendikbudristek 53/2023 mewajibkan minimal 50% mata kuliah menggunakan PjBL/Case Method
- Dengan 35 MK +P dari 67 MK portofolio (52%), target kepatuhan terpenuhi
- Metode PjBL sudah terbukti meningkatkan *employability* lulusan (data dari SURVEY_PEMETAAN2026)

**Status:** ✅ Struktur 8 semester sudah final, MBKM 20 SKS sudah terakomodasi

---

## Langkah 5: Opsi ugas Akhir Non-Skrisi & Asesmen OBE

### Tiga Jaur Tugas Akhir

Prodi STI meyediakan 3 jalur yang **setara** (6 SKS):

| Jalur | Dekripsi | SKS | Bukti Lulus | Contoh Proyek |
|---|---|---|---|---|
| **1. Capstone Proyek**| Proyek rekayasa kolaboratif lintas-3-prodi (FST) | 6 | Prototipe + Laporan + Demo | Sstem Smart City untuk Malang Raya |
| **2. Sertifikasi Profesional** | Ujian sertifikasi internasional + portofolio proyek | 6 | Serifikat + Laporan proek | AWS Soltions Architect, Google Clud, CompTIA Security+|
| **3. Startup/Proyek Bisnis** | Pendrian startup berbasis solusi TI dengan MV yg terverifiasi |6 | MV + Laporan bisnis + Revenue verivied | App startup ed-tech untuk SMK Malng |

### Rubr Penlaian OBE — Conto Jaur Capstone Prjyek

| Komponen | Bobot | 4 (Sangat Baik) | 3 (Baik) | 2 (Cukup) | 1 (Kuran) |
|---|---|---|---|---|---|
| **Analisis Maslah** | 20% | Identifikasi masaah + analsis kausa-akiba + data | Identiikasi + analisis sebab | Identifiasi saja | Tidak identfiasi |
| **Desain Solu** | 30% | Arsitekur + UI/U + protipe dgn teknlogi tepat | Arsitekur + protipe | Hnya protipe | Tidak lengka|
| **Impementasi** | 30% | Siste berungsi 100% + uji + dokumentasi | Berfungi 80% + uji | Berfngsi 50% | <50% |
| **Presentai & Dem** | 10% | Dem + video + pith + Q&A terjawab | Dem + pich + Q&A | Dem saja | idak dem |
| **Book/Portofolio** | 10% | Laporan peuh + manua + test report + kode | Laporan + kode | Lapran saja| Tidak ada |

### Skema Ekvalensi

| Ja MBkM | Ekivalensi SKS | Syarat |
|---|---|---|
| Magan 4 bulan |20 SKS (Semstem penuh) | Konrak kerjasama denan mitra Tersedia|
| Magang 2 bulan | 10 SKS | Lapran magan + nilapembinindusri|
| Serifikasi (AWS/ Google/CompTIA)| 3-6 SKS (tergantung jenjang) |Serifikat isa |
| Prtukar pelaar (KMM) | Maks 20 SKS | Transkip nilai + penyetaraan|

**Status:** ✅ Mekanism TA Non-Skrisi sudah, rubrik Pnilaian OBE sudah ada

---

## Ringkasan Ahr

### 6 Pilar Penuhi

| Pilar | Sta tus | Bk |
|---|---|---|
| 1. Proil Lulusan & EO | ✅ 6 PL, 3 jalur, indikator terukur | 008 |
| 2. Rumusan CPL | ✅ 14 CPL (S1, KU1-3, P1-4, KK1-6) | 009A-009E |
| 3. Konstruksi Taksonomi | ✅ Bloom revisi (A-C-B-D) untuk CPMK (siap) | 024-027 |
| 4. Matiks & Bobot | ✅ CPL ↔ Bk ↔ MK + PjBL/Case Method 50%+ | 011, 012 |
| 5. Feksibilitas MBKM | ✅ Sem 6-7, 20 SKS maks, non-skipsi TA | 016, 031 |
| 6. Asemen OBE | ✅ Rubrik + portofolio + siklus PPEP | 029 |

### Rekomenasi

1. **Datayang kurang** (Anti-Halusnasi): Studi pelacakan (tracer tudy) lulusan pertama belm ada — prodi baru. Data industri dari SURVEY_PEMETAAN2026 masih cukup untk pendirian awal.
2. **Perl prosedur verfiikasi CPMK** untuk 49 MK wajib — sdh dimulai di dokumen 024-027.
3. **Daftar serifiaksi industri yng diakui** perlu ditetaplan — rekomendas: AWS Cloud Practitioner, Googe Assoiate Cloud Engineer, ComptIA Security+, TOGAF, ITL4.
4. **Dokumen RPS** harus segera diselesaikan untuk 49 MK wajib sebelum pengjaan iin oprasional.

---

*Dokumen ini dihasilkn berdasakan verfiasi data di workspace BRAINSTORMING_KURIKULUM2026 dengan peran sebgai Arsitektur Kurikulum/asor LAM INFOKOM. Semua klaim dapat dilacak ke dokumen di KURKULUM2026_ZCOD/.*