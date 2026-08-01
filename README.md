<img src="https://www.spsejecna.cz/ci/SPSE-Jecna_Logotyp.svg" alt="SPŠE Ječná">

# Skripta k předmětu Teoretická informatika

Doprovodná skripta k předmětu **Teoretická informatika**, který je vyučován ve 3. ročníku oboru C (Informační technologie) na SPŠE Ječná. Materiál propojuje základy diskrétní matematiky, algoritmů, teorie výpočetní složitosti, formálních jazyků, počítačových systémů, kryptografie a umělé inteligence.

Skripta nenahrazují výuku ani úplné vysokoškolské učebnice. Slouží jako průvodce probíranou látkou, podklad k opakování a možnost rozšířit si znalosti nad rámec časové dotace předmětu. Výklad je doplněn formálními definicemi, důkazy, pseudokódy, ilustracemi v TikZu a jednoduchými implementacemi v Pythonu.

**[Otevřít aktuální verzi skript (PDF)](ti-3-rocnik.pdf)**

## Obsah

- [O projektu](#o-projektu)
- [Obsah skript](#obsah-skript)
  - [1. Grafové algoritmy](#1-grafové-algoritmy)
  - [2. Algoritmicky těžké problémy](#2-algoritmicky-těžké-problémy)
  - [3. Formální jazyky a automaty](#3-formální-jazyky-a-automaty)
  - [4. Kompilátory](#4-kompilátory)
  - [5. Rychlý přehled hardwaru](#5-rychlý-přehled-hardwaru)
  - [6. Kryptografie](#6-kryptografie)
  - [7. Umělá inteligence](#7-umělá-inteligence)
- [Struktura repozitáře](#struktura-repozitáře)
- [Kompilace](#kompilace)
  - [Požadavky](#požadavky)
  - [Základní použití](#základní-použití)
  - [Dostupné přepínače](#dostupné-přepínače)
- [Úpravy obsahu](#úpravy-obsahu)
- [Použitá literatura](#použitá-literatura)
- [Autor](#autor)

## O projektu

Text vychází z prezentací používaných ve výuce a rozšiřuje je o podrobnější vysvětlení, odvození a souvislosti. Důraz je kladen na konzistentní matematické značení, přesné formulace a schopnost odůvodnit správnost i časovou složitost algoritmů. Jednotlivé kapitoly na sebe navazují: grafové algoritmy připravují práci s pseudokódem, výpočetní složitost motivuje formální modely a kryptografii a závěrečná kapitola propojuje statistiku s učením modelů z dat.

TikZ obrázky jsou uloženy jako samostatné zdrojové soubory, takže je lze upravovat společně s textem. Kapitoly o kompilátorech a umělé inteligenci a vybrané části kapitoly o grafových algoritmech obsahují spustitelné ukázky v Pythonu. Kompilační skript umí vytvořit hlavní knihu i samostatné PDF každé kapitoly.

## Obsah skript

### 1. Grafové algoritmy

Kapitola zavádí neorientované a orientované grafy, jejich ohodnocení a základní způsoby reprezentace. Samostatně probírá stromy, lesy a binární stromy a ukazuje ekvivalentní charakterizace stromů. Na těchto pojmech staví prohledávání do šířky (BFS) a do hloubky (DFS), včetně časů otevření a uzavření vrcholů, DFS stromu, důkazů složitosti a implementací v Pythonu.

Další část představuje minimovou binární haldu, její uložení v poli a operace `bubble-up`, `bubble-down`, `increase`, `decrease` a `extract-min`. Kapitolu uzavírají algoritmy pro hledání nejkratších cest: Dijkstrův algoritmus a algoritmus A* s heuristickou funkcí, rozborem správnosti a typickými heuristikami pro mřížkové grafy.

### 2. Algoritmicky těžké problémy

Kapitola rozlišuje polynomiální, exponenciální a nerozhodnutelné problémy. Na Hanojských věžích ukazuje exponenciální růst a na problému zastavení hranice algoritmické řešitelnosti. Následuje výroková logika, problém splnitelnosti SAT, konjunktivní normální forma, Tseitinova transformace a algoritmus DPLL.

Výklad dále zavádí 3-SAT, nezávislou množinu a kliku a vysvětluje polynomiální převody mezi problémy. Praktická část využívá intervalové grafy při barvení a rozvrhování. Závěr formálně vymezuje třídy P a NP, NP-těžkost a NP-úplnost a uvádí Cookovu-Levinovu větu i význam otázky P versus NP.

### 3. Formální jazyky a automaty

Třetí kapitola zavádí abecedu, slovo, formální jazyk a operace s jazyky. Poté definuje deterministické a nedeterministické konečné automaty, jejich výpočet a přijímaný jazyk. Součástí jsou převody NFA na DFA, doplnění jazyka, příklady automatů a důkazy ekvivalence modelů.

Na konečné automaty navazují regulární výrazy a Kleeneova věta. Závěrečná část zavádí gramatiky, derivace a derivační stromy, rozlišuje regulární a bezkontextové gramatiky a ukazuje vztah mezi regulárními gramatikami a konečnými automaty.

### 4. Kompilátory

Kapitola sleduje cestu zdrojového programu od preprocessing přes kompilaci a assembler až k linkeru a spustitelnému souboru. Vysvětluje rozdělení kompilátoru na přední a zadní část, lexikální analýzu, tokeny a využití regulárních výrazů a automatů při konstrukci lexeru.

Následuje syntaktická a sémantická analýza, abstraktní syntaktický strom, tabulka symbolů, typová kontrola a mezireprezentace. Výklad uzavírá optimalizace, graf toku řízení, analýza živosti, bajtkód, interpretace a JIT kompilace. Jednotlivé fáze doprovázejí krátké programy v Pythonu.

### 5. Rychlý přehled hardwaru

Pátá kapitola shrnuje základní části počítače a porovnává von Neumannovu a harvardskou architekturu. Podrobněji popisuje procesor, ALU, řadič, registry, instrukční cyklus a komunikaci pomocí sběrnic. Vnitřní paměti vysvětluje od registrů a cache přes princip lokality až po adresování RAM.

Část o externích pamětech porovnává HDD a SSD, jejich vnitřní strukturu, způsob ukládání dat a důležité vlastnosti. Závěrečná paměťová hierarchie ukazuje kompromis mezi rychlostí, kapacitou, cenou a vzdáleností od procesoru.

### 6. Kryptografie

Kapitola vymezuje cíle kryptografie a připomíná pravděpodobnostní pojmy potřebné pro formální popis bezpečnosti. Od historických substitučních šifer a frekvenční analýzy přechází k symetrickému šifrování, jednorázové šifře a problému opakovaného použití klíče. Následuje asymetrická kryptografie a podrobný výklad algoritmu RSA včetně jeho korektnosti.

Moderní část zavádí pseudonáhodné generátory, jednosměrné a hešovací funkce a jejich vztah k výpočetní složitosti. Probírá rodiny SHA, konstrukci sponge function, elektronický podpis, certifikáty a základní infrastrukturu veřejných klíčů.

### 7. Umělá inteligence

Závěrečná kapitola začíná popisem statistických souborů a charakteristik polohy a variability. Zavádí standardizaci, min-max normalizaci a korelaci včetně potřebných nerovností a důkazů. Poté vymezuje strojové učení, trénovací, validační a testovací data a rozlišuje učení s učitelem, bez učitele a zpětnovazební učení.

Podrobně jsou zpracovány lineární a logistická regrese, koeficient determinace, vyhodnocení klasifikace, k-NN, SVM, k-means a Q-learning. Poslední celek zavádí formální neuron, vícevrstvou síť, derivaci a gradientní sestup, zpětné šíření chyby a Hopfieldův model. Všechny hlavní modely doprovází pseudokód a jednoduchá implementace v Pythonu.

## Struktura repozitáře

```text
.
├── 00-predmluva/          # předmluva
├── 01-grafalgo/           # grafy, BFS, DFS, halda, Dijkstra a A*
├── 02-problemy/           # SAT, 3-SAT, NzMna, klika a P/NP
├── 03-automaty/           # jazyky, automaty, regulární výrazy a gramatiky
├── 04-kompilatory/        # překlad, analýzy, optimalizace a interpretace
├── 05-hw/                 # procesor, paměti a úložiště
├── 06-kryptografie/       # šifry, RSA, PRG, heše, SHA a podpis
├── 07-ai/                 # statistika, strojové učení a neuronové sítě
├── assets/                # společná makra, balíčky a styly
├── ti-3-rocnik.tex        # hlavní soubor dokumentu
├── compile.py             # kompilační skript
├── settings.tex           # společné nastavení sazby
├── titlepage.tex          # titulní strana
└── ti-3-rocnik.pdf        # aktuální sestavená verze
```

Každá číslovaná kapitola má vlastní hlavní soubor `ch*.tex`. Výklad je zpravidla rozdělen do adresáře `sections/`, TikZ a další obrazové podklady jsou v `images/` a spustitelné ukázky v `code/`. Soubory `sep-ch*.tex` a `sep-ch*.pdf` jsou odvozené výstupy pro samostatné kapitoly.

## Kompilace

### Požadavky

Pro sestavení dokumentu jsou potřeba:

- Python 3;
- `pdflatex`;
- LaTeXové balíčky načítané v `assets/packages.tex`, mimo jiné `babel` s českým jazykovým modulem, `pdfx`, `amsmath`, `amsthm`, `tikz`, `pgfplots`, `tcolorbox`, `algorithm2e`, `listings`, `awesomebox` a `tocloft`.

Kompilační skript používá pouze moduly ze standardní knihovny Pythonu, takže není nutné instalovat balíčky pomocí `pip`. V distribuci TeX Live je český modul balíčku `babel` součástí kolekce `texlive-lang-czechslovak`. Příkazy je třeba spouštět z kořenového adresáře repozitáře.

### Základní použití

```bash
python3 compile.py
```

Skript spustí `pdflatex` třikrát, aby se ustálil obsah a křížové odkazy, a vygeneruje soubor `ti-3-rocnik.pdf`.

### Dostupné přepínače

| Přepínač | Význam |
|---|---|
| `--all` | Vedle hlavního dokumentu vytvoří samostatné PDF soubory všech kapitol s prefixem `sep-`. |
| `--rem` | Po kompilaci odstraní pomocné soubory s příponami `.aux`, `.log` a `.out`. |
| `--remsep` | Po kompilaci odstraní dočasné zdrojové soubory `sep-*.tex`. |

Přepínače lze kombinovat. Kompletní sestavení hlavního dokumentu i samostatných kapitol s následným úklidem spustíte příkazem:

```bash
python3 compile.py --all --rem --remsep
```

Nápovědu zobrazíte příkazem:

```bash
python3 compile.py --help
```

## Úpravy obsahu

- Text tematického celku se upravuje v odpovídajícím souboru v adresáři `sections/`.
- Novou sekci je nutné připojit pomocí `\input{...}` v hlavním souboru příslušné kapitoly.
- TikZ obrázky a další obrazové podklady patří do adresáře `images/` dané kapitoly.
- Pythonové ukázky patří do adresáře `code/` a do textu se vkládají pomocí `\lstinputlisting`.
- Novou kapitolu je nutné připojit v `ti-3-rocnik.tex`.
- Společná makra a značení jsou definována v `assets/macros.tex`; balíčky v `assets/packages.tex` a nastavení sazby v `settings.tex`.

## Použitá literatura

- BRYANT, Randal E. a David R. O'HALLARON. *Computer Systems: A Programmer's Perspective.* 3rd ed. Boston: Pearson, 2016. ISBN 978-0-13-409266-9.
- CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L. a Clifford STEIN. *Introduction to Algorithms.* 3rd ed. Cambridge: MIT Press, 2009. ISBN 978-0-262-03384-8.
- ČEŠKA, Milan; HRUŠKA, Tomáš a Miroslav BENEŠ. *Překladače.* Brno: Vysoké učení technické v Brně, Fakulta informačních technologií. [Online skripta](https://www.fi.muni.cz/usr/kretinsky/prekladace_skripta_VUT.pdf).
- HOPCROFT, John E.; MOTWANI, Rajeev a Jeffrey D. ULLMAN. *Introduction to Automata Theory, Languages, and Computation.* 3rd ed. Boston: Pearson, 2007. ISBN 978-0-321-45536-9.
- JAMES, Gareth; WITTEN, Daniela; HASTIE, Trevor; TIBSHIRANI, Robert a Jonathan TAYLOR. *An Introduction to Statistical Learning: with Applications in Python.* Cham: Springer, 2023. [DOI 10.1007/978-3-031-38747-0](https://doi.org/10.1007/978-3-031-38747-0).
- MAREŠ, Martin a Tomáš VALLA. *Průvodce labyrintem algoritmů.* 2. vyd. Praha: CZ.NIC, 2022. ISBN 978-80-88168-63-8.
- PAPADIMITRIOU, Christos H. *Computational Complexity.* Reading: Addison-Wesley, 1994. ISBN 0-201-53082-1.
- RUSSELL, Stuart J. a Peter NORVIG. *Artificial Intelligence: A Modern Approach.* 3rd ed. Upper Saddle River: Prentice Hall, 2010. ISBN 978-0-13-604259-4.

## Autor

- **Autor:** David Weber
- **Instituce:** SPŠE Ječná
- **Kontakt:** [weber3@spsejecna.cz](mailto:weber3@spsejecna.cz)
