# Bu dersi kecmeye baslamadan once asagidaki terminlerin ne olduguna baxaq.

#? 1. PROCESS           - process ve processor terminlerini sehf salmayin. Processor cihazdir. Process ise bas veren hadisedir.
#?                        Yəni, her hansisa bir proqramin iwlemesine, icra olunmasina process deyiller. Process-ler processor-larin
#?                        icinde bas verir. Processor proqramin proecess-i vaxti elde etdiyi melumati suzgecden kecirerek neticeni
#?                        istifadeciye verir.
#?                        Her PROCESSOR-da en azi bir NÜVƏ (core) olur. PROCESSOR-lar ozeklerine gore bele olur:
#?                        Cüt nüvəli = dual-core (2)
#?                        Dörd nüvəli = quad-core (4)
#?                        Altı nüvəli = hexa-core (6)
#?                        Sekkiz nüvəli = octa-core (8) ve.s
#?                        aPROCESS-ler bu core-ler vasitesi ile işləyir. 
#?                        
#?                        Her CORE 1 PROCESS icra edə bilir.
#?                        CORE-lerin çox olmasi, eyni vaxtda 1-den cox ferqli ve yaxud eyni PROCESS-i icra etmeye imkan yaradir. 
#?                        
#?                        1 CORE öz içində fərqli iş parçalarına bölunur. Bu parcalarin her biri de ayri ayriliqda ferqli PROCESS icra edir.
#?                        Core içindəki parçaların sayı PROCESSOR-un novunden, modelinden asilir olaraq dəyişə bilir.

  

#? 2. COMPILER          - Kompilyator, yəni, yazmis oldugumuz kodun, proqram halina salinmasina deyilir. Yazmis oldugumuz kodu,
#?                        istifadecinin bawa duweceyi bir formaya salinmasi ucun, COMPILER edirik. Meselen, "VisualStudio.exe"
#?                        VisualStudio proqrami kodlar vasitesi ile yaradilib ancaq biz bu kodlari gormuruk. Biz hemin kodlarin
#?                        compiler olunmus halini goruruk. Sonra bu proqrami iwe salaraq komputere qurawdiririq.


#? 3. SYNCHRON (sync)   - fərqli proqramların ardıcıl işləməsinə deyilir. Yəni bir proqram öz işini bitirmədən ikinci proqram işləməz.


#? 4. ASYNCHRON (asyn)  - ferqli proqramlarin eyni vaxtda işləməsinə deyilir. Yəni bir proqramın öz işini bitirməsini gozlemeden ikinci 
#?                        proqramın da birinci proqram ile eyni vaxtda işləməsine deyilir.


#? 5. THREADING         - 1 CORE içinde bir-birindən asılı olmadan işləyən iş parçalarına "thread" deyilir.  


#? 6. MULTITHREADING    - 1-dən çox CORE-lerin eyni vaxtda ferqli iş parçalarını işlətməsinə "multithreading" deyilir.  