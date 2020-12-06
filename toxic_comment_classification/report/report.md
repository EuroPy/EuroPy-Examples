# EuroPy Test Report

## Model Card

### Model Details


**Organization**: Northwestern University

**Authors**:

* Matthew Alvarez (matt@email.com)
* Jenny Lam (jenny@email.com)
* Sundar Rajar (sundar@email.com)
* Blaine Rothrock (blaine@email.com)


**Created Date**: 2020-11-15 10:20:56.836960

**Version**: 0.0.1

**Citation**: 
```
@cite{}
```

**Model License**: Apache License Version 2.0

**Model URL**: http://sample.com

**Data License**: Apache License Version 2.0

**Data URL**: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data

**Description**:

--

### Parameters


* **global**
	* pre_trained_model: bert-base-uncased
	* max_seq_len: 128
	* train_percent: 0.1
	* batch_size: 32
	* num_epochs: 1
	* label_cols: 
		* toxic
		* severe_toxic
		* obscene
		* threat
		* insult
		* identity_hate

	* test_size: 0.1
	* learning_rate: 2e-05


___
## Test Results

### Classification Report

Test precision, recall, accurarcy, and f1-score of each class as if >0.5 is considered classified as a label


**Labels**: `accuracy`

**Results**: (Success: True)


|    | label         |   accuracy |   weighted_precision |   weighted_recall |   weighted_f1_score |   support_pos |   f1_score_pos |   support_neg |   f1_score_neg |
|---:|:--------------|-----------:|---------------------:|------------------:|--------------------:|--------------:|---------------:|--------------:|---------------:|
|  0 | toxic         |   0.953181 |             0.932933 |          0.953181 |            0.941326 |          6090 |       0.104856 |        147074 |       0.975962 |
|  1 | severe_toxic  |   0.986198 |             0.995866 |          0.986198 |            0.99085  |           367 |       0.076049 |        152797 |       0.993047 |
|  2 | obscene       |   0.967629 |             0.958297 |          0.967629 |            0.96262  |          3691 |       0.116536 |        149473 |       0.983513 |
|  3 | threat        |   0.986381 |             0.997398 |          0.986381 |            0.991804 |           211 |       0.021576 |        152953 |       0.993143 |
|  4 | insult        |   0.969771 |             0.961975 |          0.969771 |            0.96559  |          3427 |       0.134256 |        149737 |       0.984617 |
|  5 | identity_hate |   0.987301 |             0.993762 |          0.987301 |            0.990191 |           712 |       0.261299 |        152452 |       0.993596 |


___
### ROC AUC

Area Under the Curve score for each classification (this was the training metric)


**Labels**: `accuracy`

**Results**: (Success: True)


|    | label         |   auc_score |
|---:|:--------------|------------:|
|  0 | toxic         |    0.884728 |
|  1 | severe_toxic  |    0.959031 |
|  2 | obscene       |    0.899214 |
|  3 | threat        |    0.939951 |
|  4 | insult        |    0.903171 |
|  5 | identity_hate |    0.979133 |


___
### Top 10 Word Counts by Label for testing data

Comparision of word counts in testing data. Includes top 10 words


**Labels**: `transparency`

**Results**: (Success: True)


|    | label         | 0_word   |   0_count | 1_word   |   1_count | 2_word   |   2_count | 3_word       |   3_count | 4_word   |   4_count | 5_word     |   5_count | 6_word   |   6_count | 7_word    |   7_count | 8_word   |   8_count | 9_word   |   9_count |
|---:|:--------------|:---------|----------:|:---------|----------:|:---------|----------:|:-------------|----------:|:---------|----------:|:-----------|----------:|:---------|----------:|:----------|----------:|:---------|----------:|:---------|----------:|
|  0 | toxic         | fuck     |     22878 | poop     |      6350 | nigger   |      5854 | fucking      |      5443 | penis    |      4662 | gay        |      4088 | suck     |      3906 | like      |      3574 | shit     |      3518 | cunt     |      3508 |
|  1 | severe_toxic  | fuck     |      1116 | die      |       333 | fucking  |       289 | motherfucker |       229 | mother   |       213 | bella      |       184 | swango   |       182 | suck      |       164 | dick     |       161 | fuckers  |       139 |
|  2 | obscene       | fuck     |     22685 | nigger   |      5729 | fucking  |      5270 | penis        |      4545 | suck     |      3729 | cunt       |      3460 | youfuck  |      3276 | shit      |      3205 | bitch    |      3099 | faggot   |      2982 |
|  3 | threat        | kill     |       392 | going    |       129 | rip      |        83 | tiny         |        83 | balls    |        83 | decapitate |        83 | fucking  |        42 | get       |        36 | cut      |        35 | life     |        35 |
|  4 | insult        | fuck     |     11486 | nigger   |      5721 | fucking  |      3553 | cunt         |      3394 | youfuck  |      3276 | suck       |      3226 | faggot   |      3052 | bitch     |      2935 | niggers  |      1922 | ass      |      1862 |
|  5 | identity_hate | nigger   |      5696 | gay      |      2293 | niggers  |      1986 | nigga        |       942 | faggot   |       862 | niggaz     |       718 | fuck     |       671 | niggerjew |       425 | gayyour  |       406 | jimbo    |       385 |


___
### Top 10 Word Counts by Label for training data

Comparision of word counts in training data. Includes top 10 words


**Labels**: `transparency`

**Results**: (Success: True)


|    | label         | 0_word   |   0_count | 1_word   |   1_count | 2_word   |   2_count | 3_word   |   3_count | 4_word   |   4_count | 5_word   |   5_count | 6_word   |   6_count | 7_word    |   7_count | 8_word   |   8_count | 9_word   |   9_count |
|---:|:--------------|:---------|----------:|:---------|----------:|:---------|----------:|:---------|----------:|:---------|----------:|:---------|----------:|:---------|----------:|:----------|----------:|:---------|----------:|:---------|----------:|
|  0 | toxic         | fuck     |      7836 | like     |      3348 | nigger   |      3189 | fucking  |      3139 | suck     |      2833 | shit     |      2626 | hate     |      2586 | wikipedia |      2188 | get      |      2182 | know     |      2003 |
|  1 | severe_toxic  | fuck     |      5725 | suck     |      2255 | shit     |      1679 | faggot   |      1439 | fucking  |      1361 | ass      |      1100 | nigger   |       969 | die       |       783 | sucks    |       727 | cock     |       636 |
|  2 | obscene       | fuck     |      7766 | fucking  |      3040 | suck     |      2648 | nigger   |      2635 | shit     |      2504 | ass      |      1545 | like     |      1477 | get       |      1328 | fat      |      1258 | know     |      1077 |
|  3 | threat        | die      |       775 | kill     |       498 | going    |       294 | block    |       169 | must     |       165 | jim      |       158 | wales    |       157 | fucking   |       136 | talk     |       111 | fuck     |       110 |
|  4 | insult        | fuck     |      6079 | nigger   |      2689 | fucking  |      2675 | suck     |      2442 | fat      |      1897 | faggot   |      1608 | like     |      1499 | hate      |      1375 | moron    |      1326 | jew      |      1270 |
|  5 | identity_hate | nigger   |      2879 | fat      |      1315 | jew      |      1282 | fuck     |       817 | die      |       675 | faggot   |       602 | gay      |       529 | fucking   |       513 | huge     |       429 | suck     |       419 |


___
### Classification Counts by Training Actuals, Testing Actuals, and Training Predictions

Uses a threshold of 0.75 to determine classification


**Labels**: `data-bias`

**Results**: (Success: True)




#### Figures



**Class_Distribution_Class_Only**

![Class_Distribution_Class_Only](figures/Class_Distribution_Class_Only.png)



___
### Classification Counts by Training Actuals, Testing Actuals, and Training Predictions -- Includes No Classification

Uses a threshold of 0.75 to determine classification


**Labels**: `data-bias`

**Results**: (Success: True)




#### Figures



**Class_Distribution_With_Non_Class**

![Class_Distribution_With_Non_Class](figures/Class_Distribution_With_Non_Class.png)



___
### Easily identifable non-toxic phrases

Phrases should be very low probability in every category


**Labels**: `minimum-functionality`

**Results**: (Success: True)


|    | phrase                                                                                                                                                                                                                                                                                            |   toxic |   severe_toxic |   obscene |   threat |   insult |   identity_hate |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------:|---------------:|----------:|---------:|---------:|----------------:|
|  0 | Hey, it was nice to see you the other day                                                                                                                                                                                                                                                         |    0    |              0 |         0 |        0 |        0 |               0 |
|  1 | whoa, I never thought of that                                                                                                                                                                                                                                                                     |    0    |              0 |         0 |        0 |        0 |               0 |
|  2 | very cool idea                                                                                                                                                                                                                                                                                    |    0    |              0 |         0 |        0 |        0 |               0 |
|  3 | In general I dissagree, but I understand where you are coming from.                                                                                                                                                                                                                               |    0    |              0 |         0 |        0 |        0 |               0 |
|  4 | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod                                                                                                                                                                                                                           |    0.01 |              0 |         0 |        0 |        0 |               0 |
|  5 | quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima |    0.01 |              0 |         0 |        0 |        0 |               0 |


___
### Easily Identify toxic comment phrases

Phrases pulled from the tests set.


**Labels**: `minimum-functionality`

**Results**: (Success: True)


|    | phrase                                                                                                                                                                                                                                                                                                                                                                          |   toxic |   severe_toxic |   obscene |   threat |   insult |   identity_hate |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------:|---------------:|----------:|---------:|---------:|----------------:|
|  0 | == Arabs are committing genocide in Iraq, but no protests in Europe. ==                                                                                                                                                                                                                                                                                                         |    0.78 |           0.01 |      0.03 |     0.04 |     0.06 |            0.22 |
|    |                                                                                                                                                                                                                                                                                                                                                                                 |         |                |           |          |          |                 |
|    |  May Europe also burn in hell.                                                                                                                                                                                                                                                                                                                                                  |         |                |           |          |          |                 |
|  1 | HE IS A GHAY ASS FUCKER@@!!                                                                                                                                                                                                                                                                                                                                                     |    0.99 |           0.3  |      0.98 |     0.01 |     0.89 |            0.03 |
|  2 | Simple: You are stupid!                                                                                                                                                                                                                                                                                                                                                         |    0.98 |           0.03 |      0.48 |     0    |     0.89 |            0.01 |
|  3 | MEL GIBSON IS A NAZI BITCH WHO MAKES SHITTY MOVIES. HE HAS SO MUCH BUTTSEX THAT HIS ASSHOLE IS NOW BIG ENOUGH TO BE CONSIDERED A COUNTRY.                                                                                                                                                                                                                                       |    0.99 |           0.27 |      0.96 |     0.02 |     0.9  |            0.33 |
|  4 | Yo bitch Ja Rule is more succesful then you'll ever be whats up with you and hating you sad mofuckas...i should bitch slap ur pethedic white faces and get you to kiss my ass you guys sicken me. Ja rule is about pride in da music man. dont diss that shit on him. and nothin is wrong bein like tupac he was a brother too...fuckin white boys get things right next time., |    1    |           0.39 |      0.97 |     0.04 |     0.92 |            0.29 |
|  5 | == wat the heck? ==                                                                                                                                                                                                                                                                                                                                                             |    0.96 |           0.03 |      0.79 |     0.02 |     0.47 |            0.01 |
|    |                                                                                                                                                                                                                                                                                                                                                                                 |         |                |           |          |          |                 |
|    |  what the hell is wrong with you?                                                                                                                                                                                                                                                                                                                                               |         |                |           |          |          |                 |
|    |                                                                                                                                                                                                                                                                                                                                                                                 |         |                |           |          |          |                 |
|    |  Next time you vandalize my page i'm going over there to Fayetteville, Arkansas and beating the crap out of you!                                                                                                                                                                                                                                                                |         |                |           |          |          |                 |
|  6 | If ya not... still fu*k u                                                                                                                                                                                                                                                                                                                                                       |    0.94 |           0.06 |      0.91 |     0    |     0.33 |            0.02 |
|  7 | :Eek, but shes cute in an earthy kind of way. Cant sing for shit though. Thanks for giving me an unhappy memory.                                                                                                                                                                                                                                                                |    0.45 |           0.01 |      0.37 |     0    |     0.08 |            0    |


___
### Model results to subtle put downs

Identified by Erin Leonard Ph.D. ([Psychology Today](https://www.psychologytoday.com/us/blog/peaceful-parenting/201902/backhanded-comments-digs-and-subtle-put-downs))


**Labels**: `minimum-functionality`

**Results**: (Success: True)


|    | phrase                                                                          |   toxic |   severe_toxic |   obscene |   threat |   insult |   identity_hate |
|---:|:--------------------------------------------------------------------------------|--------:|---------------:|----------:|---------:|---------:|----------------:|
|  0 | You'd be such a great supervisor if you only knew how to be strong with people. |    0.02 |              0 |         0 |        0 |     0    |               0 |
|  1 | Why are you so quiet? You need to wake up.                                      |    0.13 |              0 |         0 |        0 |     0.01 |               0 |
|  2 | If you had more heart, you’d be a great runner.                                 |    0.02 |              0 |         0 |        0 |     0    |               0 |
|  3 | You’d be so pretty if you grew out your hair.                                   |    0.1  |              0 |         0 |        0 |     0.02 |               0 |
|  4 | I’m so sorry to hear about your divorce. Your poor kids.                        |    0.17 |              0 |         0 |        0 |     0.02 |               0 |


___
### Toxic Phrases in Spanish

Same phrases from `Easily Identify toxic comment phrases`, translated to Spanish using Google Translate.


**Labels**: `bias`

**Results**: (Success: True)


|    | phrase                                                                                                                                                                                                                                                                                                                                                                                                     |   toxic |   severe_toxic |   obscene |   threat |   insult |   identity_hate |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------:|---------------:|----------:|---------:|---------:|----------------:|
|  0 | == Los árabes están cometiendo genocidio en Irak, pero no hay protestas en Europa. == \ n \ n Que Europa también arda en el infierno                                                                                                                                                                                                                                                                       |    0.03 |           0    |      0    |     0    |     0    |            0    |
|  1 | ¡ES UN FUCKER GHAY ASS @ @ !!                                                                                                                                                                                                                                                                                                                                                                              |    0.99 |           0.24 |      0.98 |     0.01 |     0.76 |            0.03 |
|  2 | Simple: ¡Eres estúpida!                                                                                                                                                                                                                                                                                                                                                                                    |    0    |           0    |      0    |     0    |     0    |            0    |
|  3 | MEL GIBSON ES UNA PERRA NAZI QUE HACE PELÍCULAS DE MIERDA. TIENE TANTO BUTTSEX QUE SU CULO AHORA ES LO SUFICIENTE GRANDE PARA SER CONSIDERADO UN PAÍS.                                                                                                                                                                                                                                                     |    0.06 |           0    |      0.01 |     0    |     0.01 |            0    |
|  4 | Tu puta Ja Rule es más exitosa de lo que nunca estarás contigo y odiándote, mofuckas tristes ... Debería abofetear tus rostros pálidos y piadosos y hacer que me beses el trasero, chicos, me enferman. Ja rule se trata de orgullo por el músico. no le digas esa mierda. y no hay nada malo en ser como Tupac, él también era un hermano ... jodidos chicos blancos hacen las cosas bien la próxima vez. |    0.39 |           0.01 |      0.23 |     0    |     0.06 |            0.01 |
|  5 | == ¿qué diablos? == \ n \ n ¿qué diablos te pasa? \ n \ n ¡La próxima vez que destroces mi página, iré a Fayetteville, Arkansas y te daré una paliza!                                                                                                                                                                                                                                                      |    0.06 |           0    |      0.01 |     0    |     0.01 |            0    |


___
### Context use of the word 'bitch'

Depending on context and who is using the term, 'bitch can be offensive to empowering' -- examples from [reallifeglobal.com](https://reallifeglobal.com/btch-please-how-to-use-the-word-bitch-correctly/)


**Labels**: `bias`

**Results**: (Success: True)


|    | phrase                                                                                                     |   toxic |   severe_toxic |   obscene |   threat |   insult |   identity_hate | use                                            |
|---:|:-----------------------------------------------------------------------------------------------------------|--------:|---------------:|----------:|---------:|---------:|----------------:|:-----------------------------------------------|
|  0 | My boss bitched me out for being 10 minutes late.                                                          |    0.51 |           0    |      0.18 |        0 |     0.05 |            0    | to bitch someout out (generally not offensive) |
|  1 | that party was bitchin                                                                                     |    0.95 |           0.02 |      0.84 |        0 |     0.26 |            0.01 | Bitchin’ as an Adjective                       |
|  2 | Calculus is a bitch                                                                                        |    0.98 |           0.09 |      0.94 |        0 |     0.73 |            0.01 | Life’s a Bitch                                 |
|  3 | Monday morning is a bitch                                                                                  |    0.98 |           0.11 |      0.95 |        0 |     0.74 |            0.01 | Life’s a Bitch                                 |
|  4 | I do everything for my boss. My friends at work tell me that I'm his bitch                                 |    0.94 |           0.02 |      0.78 |        0 |     0.42 |            0    | calling a man a bitch                          |
|  5 | 12 hours in the car today and my friends made me ride bitch that whole time.                               |    0.88 |           0.02 |      0.77 |        0 |     0.2  |            0    | to ride bitch in a car (middle back-seat)      |
|  6 | You’re being really bitchy today. Why can’t you be nicer to me?                                            |    0.83 |           0.01 |      0.37 |        0 |     0.4  |            0    | Bitchy/ing as an Adjective                     |
|  7 | I wish people would just stop bitching and moaning about corruption in politics and do something about it. |    0.3  |           0    |      0.01 |        0 |     0.02 |            0    | Bitchy/ing as an Adjective                     |
|  8 | I don’t know what’s wrong with her. She’s being a bitch                                                    |    0.98 |           0.07 |      0.93 |        0 |     0.74 |            0.01 | calling a women a bitch: annoying/unpleasent   |


___
### Always Toxic words

identify a set of words that will always flip a non-toxic comment, by class. Classification is consider >0.5. The Latin phrase `Lorem ipsum dolor sit amet. consectetur adipiscing elit, sed do eiusmod`


**Labels**: `bias`, `transparency`

**Results**: (Success: True)


|    | label         | words                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---:|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | toxic         | {'penisfucker', 'shithead', 'shiting', 'bitching', 'bitches', 'fuckhead', 'ejaculation', 'ejaculatings', 'goddamned', 'niggaz', 'fuck-bitch', 'fuckup', 'pussy', 'niggah', 'motherfuck', 'fistfucker', 'motherfuckers', 'motherfuckka', 'tittyfucker', 'fuckingshitmotherfucker', 'fucknugget', 'dumbasses', 'masturbate', 'motherfucks', 'tittyfuck', 'fingerfuckers', 'bastard', 'fingerfucks', 'fuckers', 'blowjobs', 'fuck-tard', 'motherfuckings', 'ejaculate', 'gays', 'fuckwit', 'fagged', 'fuckmeat', 'asshole', 'shitter', 'fuckwhit', 'shitters', 'cocksucking', 'fuck-ass', 'whored', 'whore', 'jerk-off', 'niggers', 'shitey', 'shitfull', 'faggit', 'assfuck', 'shitdick', 'muthafucker', 'dickhead', 'fuck', 'mthrfucker', 'goddamn', 'cocksucker', 'shagger', 'fistfuck', 'cunt', 'whorehopper', 'shiteater', 'whores', 'stupid', 'blowjob', 'whorealicious', 'fucktard', 'fistfucked', 'fucker', 'fucked', 'fuckme', 'ejaculating', 'ass-fucker', 'mtherfucker', 'shitting', 'cocksucks', 'retarded', 'fagging', 'shitface', 'fistfuckers', 'sucking', 'moron', 'fuckin', 'cocksucked', 'bitch', 'motherfucka', 'masturbating', 'shits', 'fuckface', 'faggitt', 'fuckyomama', 'penis', 'm-fucking', 'ejaculated', 'shited', 'fuckoff', 'fuckpuppet', 'douchebag', 'niggas', 'fucking', 'sucked', 'nigga', 'fingerfuck', 'jerk off', 'mother fucker', 'crap', 'mthrfucking', 'fuckhole', 'shitfucker', 'whoreface', 'dumbass', 'fistfucks', 'shitty', 'suck', 'fucktrophy', 'fuckheads', 'fingerfucker', 'muthafuckker', 'mutherfucker', 'fagots', 'jackass', 'mutherfucking', 'fucknut', 'dog-fucker', 'bull shit', 'ejaculates', 'fucka', 'vomit', 'shithole', 'faggot', 'fuckings', 'fucks', 'son-of-a-bitch', 'shitings', 'shitt', 'motherfuckin', 'muthafuckaz', 'fag', 'fingerfucked', 'shitted', 'fistfucking', 'fistfuckings', 'motherfucker', 'fagg', 'nigger', 'whorehouse', 'bullshit', 'fuckwad', 'pigfucker', 'fingerfucking', 'shit', 'fuckass', 'bitchin', 'fags', 'fannyfucker', 'motherfucked', 'shithouse', 'fucktoy', 'shitfuck', 'shite', 'assfucker', 'masturbation', 'damn', 'motherfucking'} |
|  1 | severe_toxic  | set()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  2 | obscene       | {'penisfucker', 'shithead', 'bitches', 'fuckhead', 'goddamned', 'fuck-bitch', 'fuckup', 'motherfuck', 'fistfucker', 'motherfuckers', 'motherfuckka', 'tittyfucker', 'fuckingshitmotherfucker', 'fucknugget', 'masturbate', 'motherfucks', 'tittyfuck', 'fingerfuckers', 'bastard', 'fuckers', 'blowjobs', 'fuck-tard', 'motherfuckings', 'fuckwit', 'fuckmeat', 'asshole', 'fuckwhit', 'shitters', 'cocksucking', 'fuck-ass', 'niggers', 'shitfull', 'assfuck', 'muthafucker', 'fuck', 'goddamn', 'cocksucker', 'fistfuck', 'blowjob', 'fucktard', 'fistfucked', 'fucker', 'fucked', 'fuckme', 'ass-fucker', 'mtherfucker', 'shitface', 'fistfuckers', 'fuckin', 'bitch', 'motherfucka', 'shits', 'masturbating', 'fuckface', 'faggitt', 'fuckyomama', 'penis', 'm-fucking', 'fuckoff', 'fuckpuppet', 'fucking', 'fingerfuck', 'mother fucker', 'mthrfucking', 'fuckhole', 'shitfucker', 'dumbass', 'fistfucks', 'suck', 'fucktrophy', 'fuckheads', 'muthafuckker', 'mutherfucker', 'fingerfucker', 'mutherfucking', 'fucknut', 'dog-fucker', 'bull shit', 'fucka', 'shithole', 'faggot', 'fuckings', 'fucks', 'son-of-a-bitch', 'shitt', 'motherfuckin', 'muthafuckaz', 'fistfucking', 'fistfuckings', 'motherfucker', 'bullshit', 'fuckwad', 'pigfucker', 'fingerfucking', 'shit', 'fuckass', 'bitchin', 'fannyfucker', 'motherfucked', 'fucktoy', 'shitfuck', 'assfucker', 'motherfucking'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|  3 | threat        | set()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  4 | insult        | {'penisfucker', 'shitfucker', 'fingerfuckers', 'fistfucker', 'mother fucker', 'motherfuckers', 'asshole', 'assfucker', 'fistfuckers', 'pigfucker', 'faggot', 'fuckingshitmotherfucker', 'fuck-bitch', 'bitch', 'motherfucker', 'cocksucker', 'son-of-a-bitch'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|  5 | identity_hate | {'nigger', 'niggers', 'niggas'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |


___


