# Obsah

- [Obsah](#obsah)
- [Teoretická informatika (skripta)](#teoretická-informatika-skripta)
  - [Shrnutí obsahu jednotlivých kapitol](#shrnutí-obsahu-jednotlivých-kapitol)
    - [Kapitola 1: Grafové algoritmy](#kapitola-1-grafové-algoritmy)
    - [Kapitola 2: Algoritmicky těžké problémy](#kapitola-2-algoritmicky-těžké-problémy)

---

# Teoretická informatika (skripta)

Elektronická skripta sepsaná pro předmět **Teoretická informatika** vyučovaný ve třetím ročníku na *SPŠE Ječná*. Materiály pokrývají látku v rozsahu probraném ve škole navíc s dodatečnými informacemi.

## Shrnutí obsahu jednotlivých kapitol

### Kapitola 1: Grafové algoritmy

První kapitola se zabývá grafovými algoritmy, které jsou základem mnoha úloh v informatice. Nejprve se věnuje definici grafů, jejich reprezentaci pomocí matic sousednosti, matic incidence a seznamů sousedů, a porovnává efektivitu těchto metod v různých situacích. Dále se kapitola zaměřuje na stromy jako speciální typ grafů, přičemž se rozebírají jejich základní vlastnosti, včetně lesů a binárních stromů.

Následuje popis algoritmů pro prohledávání grafů, konkrétně prohledávání do šířky (BFS) a do hloubky (DFS), které jsou klíčové pro nalezení cest v grafech. BFS je vhodný pro hledání nejkratší cesty v neohodnocených grafech, zatímco DFS se více hodí pro prohledávání stavového prostoru.

Další část kapitoly se zaměřuje na binární haldu, datovou strukturu umožňující efektivní vyhledávání minima nebo maxima v množině čísel. Kapitola popisuje základní operace s haldou, jako je vkládání, odstranění minima a úpravy klíčů, a rozebírá časovou složitost těchto operací.

Kapitola se také věnuje Dijkstrově algoritmu, který slouží k nalezení nejkratší cesty v ohodnoceném grafu s nezápornými hranami. Tento algoritmus je rozebrán z hlediska správnosti a časové složitosti, přičemž se zvažují různé způsoby jeho implementace, například pomocí seznamu nebo binární haldy.

Poslední část kapitoly představuje algoritmus A\*, verzi Dijkstrova algoritmu, která využívá heuristickou funkci pro hledání nejkratší cesty k cílovému vrcholu. Kapitola zahrnuje diskusi o správnosti algoritmu a uvádí příklady vhodných heuristik.

### Kapitola 2: Algoritmicky těžké problémy

Druhá kapitola se zabývá algoritmicky těžkými problémy, zejména problémem splnitelnosti (SAT), který je základním problémem v oblasti logiky a teorie výpočetní složitosti. Kapitola popisuje konjunktivní normální formu (CNF) a transformace do této formy, jako je Tseitinova transformace. Dále se zaměřuje na algoritmus DPLL, který je základní metodou pro řešení problému SAT, a popisuje jeho varianty a optimalizace.

Následně kapitola přechází k problému 3-SAT, který je speciálním případem SAT, kde každá klauzule obsahuje přesně tři literály. Je zde vysvětlen převod SAT na 3-SAT a diskutují se důsledky tohoto problému pro složitostní třídu NP.

Další část kapitoly se věnuje problému nezávislé množiny v grafu (NzMna), což je úloha hledání největší množiny vrcholů, mezi nimiž neexistuje žádná hrana. Kapitola uvádí převod 3-SAT na NzMna a zmiňuje aplikace, jako je barvení intervalového grafu.

Kapitola dále rozebírá problém kliky v grafu, který spočívá v nalezení největší úplné podmnožiny vrcholů, kde každý vrchol je spojen hranou s každým jiným vrcholem této podmnožiny. Diskutuje se také převod problému Klika na NzMna.

Závěrečná část kapitoly se věnuje základním třídám složitosti problémů P a NP, jejich vlastnostem, a probírá, jaké problémy patří do těchto tříd. Uvádí také další NP-úplné problémy a zabývá se otázkou, zda P = NP.