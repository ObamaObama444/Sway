# ОЧЕНЬ ВАЖНО!!!  <br>         УВАЖАЕМЫЕ ЭКСПЕРТЫ, ВИД И ФУНКЦИОНАЛ МОЕЙ СИСТЕМЫ ОБНОВИЛИСЬ!!(относительно того, что написано в проекте) <br>ПРОСЬБА ПОСМОТРЕТЬ ОБНОВЛЕННЫЙ ИНТЕРФЕЙС И ВИДЕОДЕМОНСТРАЦИЮ В РАЗДЕЛЕ<BR> "[Описание итогового решения](#описание-итогового-решения)" 


<br>
<h1 align="center" id="sway">SWAY</h1>

</h1>
<h4  align="center">AI – система видеоконтроля использования средств индивидуальной защиты 
<BR>на опасных предприятиях</h4>



- [О проекте](#аннотация)
- [Актуальность](#актуальность)
- [Проблема, цель и задачи](#цель-и-задачи)
- [Целевая аудитория](#целевая-аудитория)
- [Анализ существующих решений](#анализ-существующих-решений)
-  [Дорожная карта (План реализации)](#план-реализации)
- [Технологическая основа](#технологическая-основа)
- [Описание итогового решения](#описание-итогового-решения)
- [Тесты в реальных условиях](#тесты-в-реальных-условиях)
- [Установка и запуск локально](#установка-и-запуск-локально)
- [Заключение](#заключение)
- [Перспективы проекта](#перспективы-проекта)
-  [Список литературы](#список-используемой-литературы)


## Структура файлов

Изображения и стиль для сайта:

<details>

  <summary>static</summary>

- 1.png
-  2.png
- style.css - стиль для Web-приложения

</details>

Web-приложение:

<details>
  
<summary>templates</summary>

- index.html - само Web-приложение

</details>



</details>

**main.py** -  основной код для запуска Web-приложения

**yolov8m.pt** -  используемая модель компьютерного зрений
## Аннотация



Проект **«Sway»** представляет собой AI-ассистента, разработанного для обнаружения защитной одежды (а точнее ее отсутствия) на опасных предприятиях с целью снижения травм и летальных случаев.  Решение  направлено  на  автоматизацию анализа и соответственно более оперативное обнаружение отсутствия средств индивидуальной защиты, а  использование архитектуры компьютерного зрения Yolov8 от компании Ultralytics позволяет производить детекцию объектов с высокой скоростью и точностью.

В ходе работы над проектом был проведен анализ проблем и актуальных решений, что  дало мне возможность выявить  все  нужные  функции  для  моего решения, а также показать минусы конкурентов и не повторить их. В конечном итоге реализован продукт, представляющий Web – приложение, которое может производить сигнализацию отсутствия средств индивидуальной защиты с помощью внедрения компьютерного зрения. Сервис сначала обнаруживает камеры, подключенные к компьютеру, далее пользователь может выбрать конкретные камеры(или все сразу) для дальнейшей детекции. Web – приложение выводит обработанный (по средствам модели на архитектуре Yolov8) видеопоток с выбранных камер в реальном времени.

Решение актуально, так как позволяет оперативно выявлять нарушения, минимизировать влияние человеческого фактора и упростить работу должностных лиц, чьей основной задачей является контролирование ношения средств индивидуальной защиты, что является крайне актуальным в условиях динамично развивающейся промышленной инфраструктуры современного мира, а также потому, что полностью закрывает минусы (Такие как сложная настройка, потребность в настройке и обучении или высокие технические требования) конкурентов – аналогов.

## Проблема:
Высокая вероятность получения травм на предприятиях из-за пренебрежения техникой безопасности и отсутствия СИЗ во время работы.

## Актуальность


В  современном  мире,  в условиях динамично развивающейся промышленной инфраструктуры безопасность работников становится одним из ключевых приоритетов.

Актуальность создания инструмента для автоматизации контроля за использованием защитной одежды посредством искусственного интеллекта обусловлена тем, что она позволяет оперативно выявлять нарушения, минимизировать влияние человеческого фактора и упростить работу должностных лиц, чьей основной задачей было контролировать ношение средств индивидуальной защиты, что позволит этим лицам сосредоточиться на другой полезной деятельности.

Это особенно актуально, учитывая, что По данным Социального фонда России, в 2024 году на российских производственных площадках ежегодно фиксируется порядка 35–36 тыс. несчастных случаев, при этом летальных случаев около 2 тыс.

Однако, если учитывать только несчастные случаи с серьезными последствиями, цифры будут ниже. Например, в 2024 году было зарегистрировано 4 905 таких случаев, из которых 1 036 закончились летальным исходом.
<center><img  src=  "https://github.com/user-attachments/assets/32e3425e-2acc-4619-9dad-99b68c673880" ></center>


## Цель и задачи


**Цель:**  
Разработать систему видеонаблюдения, которая определяет наличие защитной одежды у рабочих и сигнализирует об её отсутствии.

**Задачи:**  
- Проанализировать производственный процесс и определить, что нужно детектировать 
- Реализовать алгоритм детекции с использованием YOLOv8 и алгоритм сигнализации.  
- Реализовать web-приложение для визуализации работы системы
- Протестировать работу системы

## Анализ существующих решений

|               | tochka_ai                                                   | VizorLabs H&S                                                                 | NEURUS                                                      |
|---------------|-------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| **+**         | - Универсальность  <br> - Высокая точность детекции         | - Высокая точность детекции <br> - Возможность одновременной обработки большого числа потоков | - Универсальность <br> - Интеграция с другими технологиями  |
| **-**         | - Высокие технические требования <br> - Потребность в настройке и обучении | - Высокие технические требования <br> - Сложная настройка <br> - Возможная потребность в дообучении нейросети | - Потребность в настройке и обучении <br> - Высокие технические требования |

<br>
Анализ существующих решений показал, что подобные системы (системы видеоконтроля средств индивидуальной защиты) уже существуют, и даже большинство их них предоставляют неплоой функционал (представлен в таблице)
Однако, несмотря на эти преимущества, у существующих решений:


- также выявлены **существенные недостатки** (представлены в таблице)

- все системы **платные**
- Все перечисленные системы являются просто системами видеонаблюдения с компьютерным зрением, в то время как я предлагаю  ***систему видеонаблюдения с алгоритмами компьютерного зрения, способная самостоятельно сигнализировать о нарушении***

Таким образом, мой проект ориентирован на устранение указанных недостатков: 
Он предлагает **бесплатное решение с невысокими техническими требованиями, простой настройкой и высокой точностью распознавания**, что делает его более доступным и эффективным для предприятий любого уровня.

## План реализации
<center><img  src=  "https://github.com/user-attachments/assets/cbead2b4-157a-48f9-ab11-59aab0932cad" ></center>



## Целевая аудитория

- **Строительные компании:**  
   Специалисты, ответственные за безопасность и здоровье сотрудников<br> (прорабы, руководители служб охраны труда и т.д.).

-  **Производственные и промышленные предприятия:**  
   Люди, контролирующие условия работы на производстве и отвечающие за безопасность и жизни работников на конкретном участке   (Начальники цехов и специалисты по охране труда)

- **Страховые компании.**














## Технологическая основа

### Инструменты и библиотеки

***Python*** был выбран в качестве основного языка программирования, поскольку он является предпочтительным при работе с нейронными сетями благодаря своей простоте использования и многофункциональности.

Так же при реализации интерфейса использовался язык гипертекстовой разметки  ***HTML*** , так же использовался  ***JavaScript*** , ***CSS***






### Модель:

В качестве основной тестовой модели использовалась ***[YOLOv8m](https://docs.ultralytics.com/ru#yolo-a-brief-history)*** 

YOLOv8m - это модель компьютерного зрения от компании [Ultralytics](https://ultralytics.com/) 

Использование  ***YOLOv8m*** обусловлено лучшими характеристиками по сравнению с конкурентами. Модель обучена на лично собранном и размеченном датасете.
(Для разметки и аугментации использовалась платформа Roboflow)
#### Основные характеристики 
- **Общее количество параметров**: Около 26 миллионов

**Архитектура:**
  - **Backbone** (Модифицированная CSPDarknet с использованием фокусирующих слоёв для первичной обработки изображения)
  - **Neck** (Сеть типа PAN (Path Aggregation Network) для объединения признаков с разных уровней)
  - **Head** (Детектор, реализующий anchor‑free подход для точной локализации объектов)


**Сравнение архитектур компьютерного зрения:**

| Критерий      | YOLO          | SSD          | Faster R-CNN | Mask R-CNN  |
|---------------|---------------|--------------|--------------|-------------|
| **Скорость**  | ~0.022 с/изобр. <br>(~45 FPS) |0.033–0.05 с/изобр.<br>(~20–30 FPS )   | 0.1–0.2 с/изобр.<br>(~5-10 FPS )       |0.2–0.5 с/изобр.<br>(~2-5 FPS )   |
| **Точность**  | ~80%      | ~70%    | 70-85%     | 73-85%   |
| **Обнаружение** | Объекты и их местоположение в одном проходе | Объекты и их местоположение в одном проходе | Обнаружение объектов и их границ | Обнаружение объектов, их границ и сегментация |
| **Использует**  | CNN         | CNN          | CNN          | CNN         |
| **Применение**  | Реальное время, задачи, **где важна скорость** | Обнаружение в реальном времени | Задачи, требующие высокой точности | Сегментация и обнаружение объектов |

<br>

#### Главными метриками для анализа работы модели компьютерного зрения для моей задачи  являются:

-   **Скорость** — Эта метрика оценивает время, которое требуется модели для обработки одного изображения или видеокадра (что особенно важно для задач в реальном времени)
Для удобства оценки, также дополнительно выведено в системе кадров в секунду (FPS)
-   **Точность** — Метрика точности показывает, насколько правильно модель классифицирует или распознаёт объекты на изображениях (для оценки я использую метрику mAP (выраженную в процентах))
-    **Обнаружение** — Эта метрика отражает, что модель может распознавать(эту метрику я решил включить для визуализации возможностей модели, т.к. в перспективе мне понадобятся расширенные возможности модели, такие как сегментация(на данном этапе используется только возможность классификации))

 #### На основе этих данных можно сделать вывод, что модель Yolov8m лучше своих аналогов, при этом  не уступая и моделям намного больше неё.



### Минимальные требования к видеопамяти:

- **Использование:** Рекомендуется видеокарта с 6–8 ГБ VRAM (требования зависят от разрешения входных изображений и размера батча)

- **Обучение:** Для обучения модели желательно использовать GPU с 12 ГБ VRAM или более
### Минимальные требования к камере:
*Для начала хочется сказать что для различных условий (например расстояния до объектов и погоды) требования будут изменяться
-  разрешение **720p** и **30 кадров в секунду** 
- камера должна быть подключена **локально по проводу**


<br>

**Объекты детекции:**
​При разработке системы у меня не было конкретной идеи относительно того, какие именно объекты детектировать(то есть я не ориентировался на конкретного конечного заказчика/потребителя, на конкретные задачи которого заточена система). <br>Я выбрал средства индивидуальной защиты, такие как защитный шлем, перчатки и сигнальный жилет, поскольку они являются критически важными для обеспечения безопасности на рабочих местах практически в каждом предприятии(из [Целевой аудитории](#целевая-аудитория)) и широко используются в различных отраслях промышленности. 
 
**Система распознает следующие классы:**
 - Защитный шлем / Отсутствие защитного шлема  
 - Перчатки / Отсутствие перчаток  
 - Сигнальный жилет / Отсутствие сигнального жилета
 


### Библиотеки

-  ***Ultralytics*** - Python-библиотека. В проекте используется для работы с моделью YOLO

-  ***Open CV*** - библиотека для компьютерного зрения, предназначенная для обработки изображений и видеопотоков в реальном времени, в проекте используется для  захвата, анализа и обработки видеоданных

-  ***Flask*** -Легковесный фреймворк на Python, используемый для создания веб-приложений и организации серверной логики проекта, в проекте используется для реализации web - приложения

-  ***Telebot*** - Python-библиотека. В проекте используется для реализации телеграмм-бота для получения уведомлений о нарушении правил ношения СИЗ
## Описание итогового решения

На данном этапе я имею: систему детекции отсутствия СИЗ с использованием AI-алгоритмов компьютерного зрения.

**Процесс работы системы:**

 - **Обнаружение камер:**  
   С помощью OpenCV перебираются доступные устройства, проверяется возможность открытия видеопотока. Если камера стабильно выдаёт кадры, она регистрируется для использования в системе.

 - **Серверная часть:**  
   На базе Flask создаётся веб-сервер, обрабатывающий HTTP-запросы от клиентского интерфейса. При выборе камер сервер захватывает видеопотоки и передаёт их алгоритму детекции.

 - **Детекция:**  
   Алгоритмы YOLOv8 применяются к каждому кадру для выделения объектов и вычисления вероятности их обнаружения. Обработанный кадр конвертируется в формат base64 и возвращается клиенту.


<h3>Архитектура решения:


#### *Общая архитектура:*



<img src="https://github.com/user-attachments/assets/5e42f919-89eb-4d6d-b256-41dc15fc29fc" width="900" height="500"/>

#### *Подробная архитектура:*


<img src="https://github.com/user-attachments/assets/4cf57546-ea5d-42ba-8d61-30a4081b93b2" width="900" height="500"/>

 ### Интерфейс web-приложения (путь пользователя):
 Интерфейс моего web-сервиса 
 Главный экран системы сразу показывает список доступных камер, подключённых к устройству, что позволяет сразу выбрать нужные для видеонаблюдения. При наведении курсора на правую панель или нажатии на иконку в виде трёх полосок разворачивается дополнительное меню, где можно выбрать режимы работы с видео. Здесь можно запустить запись видеопотока и включить или отключить модуль компьютерного зрения, который распознаёт наличие средств индивидуальной защиты на рабочих и отправляет уведомления в Telegram при их отсутствии. При этом функция компьютерного зрения может быть отключена, если систему используют исключительно для наблюдения.

В разделе архива хранятся все записи, с возможностью сортировки по камере, времени (новые/старые) и наличию нарушений. Ниже представлены сами записи, которые можно просматривать с разной скоростью, переименовывать и удалять, при этом система указывает, зафиксированы ли на записи нарушения.

В разделе «Настройки» можно выбрать масштаб интерфейса, изменить путь сохранения видеозаписей (по умолчанию C:\Users[имя пользователя]\Videos), подобрать тему оформления и настроить уведомления в Telegram. Интерфейс будет дорабатываться, и на финальной защите я представлю вам ещё более усовершенствованное решение.

![Image](https://github.com/user-attachments/assets/482d73a1-171b-4426-a2fb-f17085ac9cc8)

![Image](https://github.com/user-attachments/assets/12fe9c02-e56e-40cc-96df-d6198986b969)

![Image](https://github.com/user-attachments/assets/decfaded-978d-4032-8d33-b4d52b8ae445)

![Image](https://github.com/user-attachments/assets/d7a0e8ac-336a-4991-9439-3af660b5e51a)

![Image](https://github.com/user-attachments/assets/173bbd08-a24f-40a3-8249-378d2a341244)

![Image](https://github.com/user-attachments/assets/6d27ce2e-6d1e-455f-98fd-cf9bf408c5db)  ![Image](https://github.com/user-attachments/assets/1918f2ef-d45f-4643-b76a-423ffd5beb0c) | ![Image](https://github.com/user-attachments/assets/ee987d41-05c8-4df0-b7fe-ca68257b5502)

![Image](https://github.com/user-attachments/assets/1f8e4a9c-eca1-40ef-a801-3932c6a0a95d)

![Image](https://github.com/user-attachments/assets/9fdd5cd4-a7a9-40e7-8507-0200e0b4e5f7)

![Image](https://github.com/user-attachments/assets/c325ae97-e1c8-471a-b715-f3261410c011)

![Image](https://github.com/user-attachments/assets/dffd9734-4c89-4ef0-9f56-7e6178df3396)

![Image](https://github.com/user-attachments/assets/e92bdc37-253f-4055-8765-1bc3e1e164c4)

![Image](https://github.com/user-attachments/assets/a4a2c820-9135-4e72-ab0c-b386b342af9b)

![Image](https://github.com/user-attachments/assets/c5cd9fc1-4d15-4448-b452-e4fd8300b17a)

![Image](https://github.com/user-attachments/assets/04ee87f5-7306-477f-b7bc-cb4125647e9d)
<br>
## Видеодемонстрация



## Сравнительный анализ моего решения с аналогами

| Метрика                             | tochka_ai | VizorLabs H&S | NEURUS | Моё решение |
|-------------------------------------|-----------|---------------|--------|-------------|
| Высокая точность детекции           | ✅        | ✅            | ✅     | ✅          |
| Многопоточность     | ❌        | ✅            | ❌     | ✅          |
| Универсальность                     | ✅        | ❌            | ✅     | ❌          |
| Интеграция с другими технологиями   | ❌        | ❌            | ✅     | ❌          |
| Невысокие технические требования    | ❌        | ❌            | ❌     | ✅          |
| Простая настройка                   | ❌        | ❌            | ❌     | ✅          |
| Бесплатно?                          | ❌        | ❌            | ❌     | ✅          |

В процессе анализа решений для системы видеоконтроля использования средств индивидуальной защиты (СИЗ) на опасных предприятиях были выбраны следующие ключевые метрики:

- **Высокая точность детекции** --- Эта метрика отражает способность модели точно идентифицировать и локализовать объекты на изображениях. Высокая точность детекции критически важна для минимизации ложных срабатываний и пропусков, обеспечивая надежный мониторинг соблюдения правил безопасности. 
Высокой точность обнаружения я считаю при **mAP** больше 75%
- **Многопоточность** --- Способность системы обрабатывать несколько видеопотоков, что позволяет одновременно контролировать несколько зон предприятия в реальном времени, что повышает общую эффективность системы видеонаблюдения

-  **Универсальность** ---  Универсальность решения подразумевает его способность адаптироваться к различным условиям эксплуатации, типам оборудования и сценариям использования. Это важно для обеспечения гибкости и масштабируемости системы в различных производственных средах
- **Интеграция с другими технологиями** --- Возможность интеграции с существующими системами безопасности (например для создания комплексной инфраструктуры мониторинга и управления).
- **Невысокие технические требования** ---  Ментика показывает, низкие ли требования к аппаратному обеспечению и камерам (что позволяет определить ее доступность для предприятий с ограниченными ресурсами)
-  **Простая настройка** --- Метрика показывает, интуитивно понятен ли процесс установки и конфигурации системы 
(простая настройка системы может существенно сократить время и затраты на процесс внедрения системы, а также снизить вероятность ошибок при настройке)

-  **Бесплатность** ---  Метрика показывает, бесплатна ли система

<br>
Выбор этих метрик обусловлен стремлением создать эффективную, доступную и легко интегрируемую систему видеоконтроля использования СИЗ, соответствующую потребностям современных промышленных предприятий. 
В конечном итоге мое решение превосходит аналоги по ключевым метрикам, что делает его лучшим среди аналогов! Осталось только протестировать систему в реальных условиях!


## Тесты в реальных условиях 

## Установка и запуск локально

  

Чтобы запустить локальную копию, выполните следующие простые шаги.

Учтите Python должен быть не менее **3.9.8**

```shell or cmd

# Клонируем репозиторий

> git clone https://github.com/ObamaObama444/Sway

  

# Перемещаемся в него

> cd Sway
  


#Устанавливаем список библиотек

> pip install -r requirements.txt


#Запускаем

> python main.py 

```


## Заключение

В ходе работы над проектом был проведен анализ проблем и актуальных решений, что дало мне возможность выявить все нужные функции для моего решения, а также показать минусы конкурентов и не повторить их. В конечном итоге реализован продукт, представляющий Web – приложение, которое может производить сигнализацию отсутствия средств индивидуальной защиты с помощью внедрения компьютерного зрения. Сервис сначала обнаруживает камеры, подключенные к компьютеру, далее пользователь может выбрать конкретные камеры(или все сразу) для дальнейшей детекции. Web – приложение выводит обработанный (по средствам модели на архитектуре Yolov8) видеопоток с выбранных камер в реальном времени.

Благодаря этому система помогает предприятиям оперативно реагировать на потенциальные угрозы. Она не только поможет опасным предприятиям автоматизировать процесс контроля ношения средств индивидуальной защиты, но и снизить риск травматизма и летальных исходов на опасных предприятиях! В ходе работы над проектом мне удалось успешно достичь всех поставленных целей, предложить свое решение поставленной проблемы и даже протестировать систему в реальных условиях!

## Перспективы проекта

- Интеграция системы КПП для идентификации конкретного сотрудника, нарушающего правила.  
-  Улучшение модели компьютерного зрения 
-   Модернизация web-приложения.



## Список используемой литературы

- **Flask Documentation (Stable):**  
  [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)
- **OpenCV Documentation:**  
  [https://docs.opencv.org/4.x/](https://docs.opencv.org/4.x/)
- **Социальный фонд России:**  
  [https://social-fund.ru/](https://social-fund.ru/)
- **Ultralytics:**  
  [https://ultralytics.com/](https://ultralytics.com/)
- **YOLOv8 Documentation:**  
  [https://docs.ultralytics.com/](https://docs.ultralytics.com/)



## Обратная связь

Если у Вас возникли вопросы по работе с системой или технические трудности, я всегда готов помочь! 
Вы можете:
- Написать мне на почту: [egalagoza5@gmail.com](mailto:egalagoza5@gmail.com)
   
- Обратиться напрямую в Telegram: [@egalagoza](https://t.me/egalagoza)

Я помогу разобраться с настройкой и использованием, а также ответить на все интересующие Вас вопросы !
<br>
<br>
<p align="center">
  <a href="#sway">НАВЕРХ</a>
</p>





  
