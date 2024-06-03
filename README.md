# **Клейн Максим, гр. 253504**

В ходе написания курсовой работы по предмету «Объектно-ориентированное программирование» была поставлена цель разработать аналог игры Galaga на языке Python. Такое задание было выбрано, потому что для создания игры не нужно пользоваться фрэймворками. Большинство функционала можно взять из библиотек, которые уже предусмотрены в языке. 

В игре Galaga пользователь управляет кораблём, который должен победить несколько врагов. А само управление кораблём происходит путём нажатия стандартных клавиш клавиатуры: вверх, вправо, вниз, влево, пробел. Если пользователь проигрывает, то высвечивается Game Over. У игрока имеется несколько жизней, который убывают в случае проигрыша. Соответственно, для создания игры нужно использовать библиотеку Pygame и графические отображения. 

Я использовал иерархическую модель данных. Так в этой модели данные организованы в виде иерархической структуры, состоящей из родительских и дочерних элементов. Каждый элемент может иметь только одного родителя, что создает дерево-подобную структуру. Это поможет показать структуру проекта и взаимосвязь его элементов. 


Создания функционала игры можно разбить на несколько пунктов: движение корабля, графическое отображение (корабль игрока, инопланетяне, взрывы и ракеты), общие параметры (вход и выход из игры, управление графическими отображениями). 


### *Для этого было создано несколько папок, включающие в себя классы:*

 + Основные классы: 

   +  Класс constants.py содержит основные объекты для отображения игры на экран: SCREEN_WIDTH, SCREEN_HIGH, FPS, SPRITE_SHEETS. SPRITE_SHEETS содержит ссылку на папку assets, хранящую отображения. 

   +  В папке assets находятся отображаемые объекты: 
          
        + Images – картинки, которые используем для отображения игровых «персонажей»;
        + Sounds – звуки, которые присутствуют в игре; 
    
    + Класс Game определяет основные методы, который представляет основной цикл игры: 
  
        + init инициализирует основные атрибуты объекта: done (завершена ли игра), screen (игровой экран), clock (объект для времени), fps (количество кадров в секунду), states (словарь текущих состояний), state_name (имя текущего состояния) и state (текущее игровое состояние).
          
        + event_loop – метод обрабатывающий игровые события. 
  
        + update - метод для обновления игрового состояния.
     
        + draw - метод для отрисовки игрового состояния на экране.
     
        + run - метод для запуска игрового цикла.
    
    + Папка states содержат основные классы для управления игрой: base_state, game_over, gameplay, menu, splash. 
        
        + BaseState представляет основные методы и атрибуты для игровых состояний в игре: init, startup, get_event, update, draw.
     
        + Класс GameOver является подклассом и представляет игровое состояние «Конец игры»: init, get_event, draw.
     
        + Класс Gameplay представляет состояние игрового процесса: init, startup, add_control_points, get_event, add_enemy, shoot_rocket, enemy_shoots, draw, drawPath, draw_control_lines, draw_score.
     
        + Класс Menu представляет состояние меню игры: _init_, render_text, get_text_position, handle_action, get_event, draw.
     
        + Класс Splash представляет состояние «заставки» игры, которое отображает заголовок на экране: init, update, draw.  
  
    + Класс Starfield отвечает за отображение звездного поля на экране игры.

         + Метод init инициализирует атрибуты класса. Он создает три коллекции звезд: star_field_slow, star_field_medium и star_field_fast, используя метод create_stars для генерации указанного количества звезд.

         + Метод create_stars генерирует указанное количество звезд. Он создает пустой список stars и в цикле указанное количество раз генерирует случайные координаты star_loc_x и star_loc_y в пределах ширины и высоты экрана.
     
         + Метод render_stars отрисовывает звезды из указанной коллекции star_collection на заданном экране screen.
     
         + Метод render отображает звездное поле на заданном экране screen. Он вызывает метод render_stars для каждой коллекции звезд с разными значениями скорости, размера и цвета.

    + Класс SpriteSheet предназначен для работы с спрайтами (графическими изображениями) в виде листа или стрипа.

       + Метод init инициализирует атрибуты класса. Он загружает изображение листа спрайтов из указанного файла filename с помощью pygame. image. load.
     
       + Метод image_at загружает конкретное изображение из указанного прямоугольника rectangle и поверхность image с таким же размером, как и прямоугольник. Затем метод копирует часть изображения из листа спрайтов, определенную прямоугольником rect, с помощью blit.
     
       + Метод images_at загружает целый набор изображений и возвращает их в виде списка. Он принимает список прямоугольников rects, каждый из которых определяет прямоугольник для загрузки изображения.
     
       + Метод load_strip загружает целый стрип изображений и возвращает их в виде списка. Он принимает параметры rect (прямоугольник, определяющий общий размер каждого изображения в стрипе), image_count (количество изображений в стрипе) и colorkey (ключевой цвет для установки прозрачности). 
      
+ Папка Sprites содерджит основные классы для работы с объектами: 
   
   + ControlPoint –  класс, который представляет отображение точки в графическом интерфейсе.
  
   + Enemy – класс, который отвечает за отображение противников.

   + Explosion – класс, которые отвечает за отображение взрыва.
  
   + Player – класс, который отвечает за отображение игрового персонажа.
  
   + Rocket – класс, который отвечает за отображение снаряда.

      
+ Папка Bezier отвечает за расположение объектов и контрольные точки, вот основные его классы: 
   
   + controll_point_handler служит для обработки индексов квартета и индекса точки управления. 
     
   + path_point_controll отвечает за представление точек пути. 

      ![image1](https://github.com/makseight89/Galaga/blob/main/Screenshot%202024-02-29%20151441.png)

Рассмотрим основные классы: 

 + Передвижение корабля (moving): 

   +  Controll_handler_mover — класс, который отвечает за перемещения точек, в которых находятся объекты:
       
       + Функция move_control_handler перемещает контрольную точку в заданные координаты.
       
       + align_all выравнивает контрольные точки на основе координат. 

    +  Сontroll_point_collection_factory – класс, который отвечает за коллекции контрольных точек: 
          
        + create_collection1, create_collection2, create_collection3, create_collection4 – коллекции, которые содержатся в классе. 
       
    
    + ControlPointQuartet – класс, который проверяет находится ли точка в пределах координат: 
  
        + Length  возвращает количество контрольных точек в квадрате. 
  
        +  is_in_control_point проверяет находится ли точка в пределах радиуса от одной контрольной точки. 
    
    + ControlPointQuartetCollection – коллекция квартетов контрольных точек:
        
        + get_quartet_from_time принимает квартет контрольных точек в зависимости от времени. 
  
        + give_position_is_inside_control_point проверяет находится ли точка в пределах контрольных точек. Если точка находится в пределах точек, метод возвращает индекс квартета, индекс точки внутри квартета и значение True. 
  
        + save_control_points – сохраняет координаты контрольной точки.
     
    + PathPointCalculator - вычисляет движение точки на пути.
  
        + Метод calculate_path_point используется для вычисления точки на пути (path point) на основе квартета контрольных точек (control_point_quartet) и времени (time_to_calculate).

   + PathPointSelector выбирает точки пути: create_key (), is_path_point (), create_path_point_ mapping (), find_related_path_point (), find_controll_points (), get_last_quartet_index(), get_number_of_quartets (), find_path_point_of_control_point (), find_control_points_of_path_point (), get_control_point_pairs (). 

       ![image2](https://github.com/makseight89/Galaga/blob/main/Screenshot%202024-02-29%20180550.png)

+ Отображение объектов (sprites): 

   +   ControlPoint –  класс, который представляет отображение точки в графическом интерфейсе:
      
        + init инициализирует различные атрибуты: координаты точек, индексы, коллекцию контрольных точек и объект перемещения контрольной точки.

        + Original_image – рисование контрольной точки.
  
        + Update – обновление состояния контрольной точки. 
 
        + get_surf – возвращает положение контрольной точки. 

  
    + Enemy – класс, который отвечает за отображение противников:


       + init инициализирует различные атрибуты противника: таймер, набор контрольных точек, интервал между кадрами, отображение, вычисление точек пути.

       + Rect отвечает за расположение в текущей точке. 
calculate_rotation отвечает за изменение положения между предыдущей и текущей точкой. 

      + get_surf – текущее отображение объекта. 


   + Explosion – класс, которые отвечает за отображение взрыва: 
        + init инициализирует различные атрибуты взрыва: таймер, интервал между изменениями кадров, количество изображений взрыва, список изображений, список текущих отображений.
  
        + sprites. Load _strip – загрузка изображений взрыв. 
  
        + update – обновления состояния взрыва. Он инкрементирует таймер и проверяет достигнут ли интервал отображения.
  
  + Player – класс, который отвечает за отображение игрового персонажа: 

       + init инициализирует различные атрибуты игрока: таймер, интервал между изменениями кадров, количество изображений игрока, cписок изображений и индекс текущего изображения.

      + Update – обновление состояния игрока на основе нажатых клавиш. Инкрементирует счётчик и перемещает игрока вправо или влево.
      
      +  get_surf – возвращает текущее отображение игрока с учётом интервала изменения кадров.
  
  + Rocket – класс, который отвечает за отображение снаряда. 
  
    + init инициализирует различные атрибуты ракеты: таймер, интервал между кадрами, количество изображений ракеты, вертикальная скорость, горизонтальная скорость, список изображений, угол поворота.

    + update отвечает за обновление состояния ракеты. Он инкрементирует таймер, перемещает прямоугольник ракеты с учетом горизонтальной и вертикальной скоростей.
  
    + get_surf возвращает текущее изображение ракеты с учетом интервала между изменениями кадров. 

    ![image3](https://github.com/makseight89/Galaga/blob/main/%D1%81%D0%BF%D1%80%D0%B0%D0%B9%D1%82%D1%8B.png)

+ В папке States находятся классы, которые отвечают за состояние в игре: base_state, game_over, gameplay, menu, splash

  + Класс BaseState для состояний игры в модуле pygame:
     
     + Конструктор init инициализирует объект класса BaseState.
   
     + Метод startup вызывается при запуске состояния и может быть переопределен в подклассах для выполнения дополнительных действий при старте состояния.
   
     + Метод get_event вызывается при получении события от модуля и может быть переопределен в подклассах для обработки определенных событий.
   
     + Метод update вызывается каждый кадр и может быть переопределен в подклассах для обновления состояния игры.
   
     + Метод draw вызывается каждый кадр для отрисовки состояния игры на поверхности. Он может быть переопределен в подклассах для отображения определенных элементов игры.
   
  + Класс GameOver расширяет его функциональность для отображения экрана «Game Over» в игре.
 
    + Конструктор init инициализирует объект класса GameOver.
   
    + Метод get_event переопределен для обработки событий.
   
    + Метод draw переопределен для отображения экрана «Game Over».
   
 + Класс Menu расширяет его функциональность для отображения меню игры:

    + Конструктор init инициализирует объект класса Menu.
  
    + Метод render_text принимает индекс пункта меню и возвращает текстовое изображение пункта меню с соответствующим цветом.
  
    + Метод get_text_position принимает текстовое изображение и индекс пункта меню и возвращает прямоугольник позиции текста, вычисленный на основе центра поверхности отображения и индекса пункта меню
  
    + Метод handle_action обрабатывает выбранный пункт меню.
  
    + Метод get_event переопределен для обработки событий.
  
    + Метод draw переопределен для отображения меню игры.
  
 + Класс Splash расширяет функциональность для отображения экрана заставки (splash screen) в игре:

    + Конструктор init инициализирует объект класса Splash.
  
    + Метод update обновляет состояние экрана заставки.
  
    + Метод draw переопределен для отображения экрана заставки.
    
    ![image4](https://github.com/makseight89/Galaga/blob/main/Screenshot%202024-02-29%20181659.png)
