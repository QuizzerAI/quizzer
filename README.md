# Quizzer

**Quizzer** è uno strumento AI che permette di creare quiz su misura direttamente dal tuo materiale di studio.

## Come funziona

**Quizzer** è composto da 3 componenti fondamentali:

1. `quizzer.py`: è lo script che trasforma i tuoi **pdf** in file **json** contententi le domande. Questo tipo di file è chiamato **airesponse**. È l'unico script che usa l'AI.
2. `packer.py`: è lo script che trasforma i tuoi **airesponse** in file **json** contententi le domande in un formato più facilmente gestibile. tale formato è chiamato **quizpack**
3. `quiz.py`: è lo script che legge i tuoi **quizpack** e ti sottopone il test.

Quindi per effettuare un test è necessario effettuare alcuni passaggi:

```txt
file.pdf --[quizzer.py]--> file.airesponse.json --[packer.py]--> file.quizpack.json
```

## Installazione

 > ATTENZIONE
 > Queste operazioni sono richieste solo se si vuole usare lo script `quizzer.py`.
 > Nel caso si voglia solo utilizzare dei file `quizpack` senza generarne di nuovi è possibile saltare l'installazione.

Una volta scaricata la repository basterà installare i pacchetti richiesti andando nella cartella della repo ed eseguendo

```sh
pip install -r requirements.txt
```

Eseguito il comando bisognerà accedere alla dashboard delle API di OpenAI e creare un nuovo assistente. Selezionare il modello desiderato (suggeriro: `gpt-4o-mini`) ed inserire sotto la voce _System instructions_ il contenuto del file  `system.prompt`.

Una volta fatto ciò bisognerà creare nella root della cartella della repo un file `.env` ed inserire due righi strutturati come segue:

```sh
OPENAI_API_KEY=sk-...MA
ASSISTANT_ID=asst_...0R
```

Sostituendo ovviamente con i valori corrispondenti che potete trovare sulla vostra dashboard.

Fatto ciò assicuratevi di avere del credito su OpenAI. Con questa configurazione lo script è molto economico, ho potuto fare test su tutto il materiale del corso di Reti di Calcolatori a soli €0,02. Scegliendo di usare `gpt-4o` potreste ottenere dei quiz meglio strutturati ma il costo è 10 volte maggiore.

## Come usarlo

Vediamo come partire con il tuo file pdf ed arrivare a svolgere il quiz sugli argomenti trattati.

### `quizzer.py`

Questo comando deve ricevere come argomento il nome del file che deve analizzare; a sua volta esso stampa in output il risultato. Un esempio d'uso:

```sh
./quizzer.py Slides/lezione16.pdf > lezione16.airesponse.json
```

### `packer.py`

Questo comando riceve sulla pipe un file _airesponse_ e stampa il quizpack associato. Esempio:

```sh
cat lezione16.airesponse.json | ./packer.py > lezione16.quizpack.json
```

### `quiz.py`

Questo comando riceve sulla pipe un file _quizpack_ ed avvia il quiz associato. Esempio:

```sh
cat lezione16.airesponse.json | ./quiz.py
```

## Perché le pipe

In fase di testing risultava la soluzione più semplice per verificare che ogni componente si comportasse come previsto. Le pipe permettono di concatenare più comandi in uno più completo. In futuro si vorrà sicuramente supportare l'input ed output su file tramite argomenti.

## Come contribuire

Chiunque voglia contribuire è libero di farlo in ogni modo: con suggerimenti, pull request, scrivendo, traducendo ed organizzando la documentazione, ed in qualsiasi altro modo!

## Cosa viene dopo?

Oltre a risolvere problemi di stabilità legati alle risposte dell'AI, sarà necessario ampliare il toolset con script che permettano di gestire con più libertà i file quizpack, in maniera da poter riarrangiare (sia in maniera ordinata che casuale), filtrare, mappare, unire e dividere i file quizpack. Migliorare la fase di setup del tool, con script di installazione automatici, e di configurazione delle API di OpenAI. Inoltre migliorare la flessibilità dei tool già esistenti sarà un altro passo molto utile per rendere questo strumento ancora più comodo: permettere di inserire file di input multipli come argomenti, permettere di specificare un file di output, utilizzare funzioni asincrone per parallelizzare le chiamate ad openai; questi sono solo alcune delle idee per migliorare il Quizzer.
