-- Задание 1: Создание процедуры для форматирования секунд в дни, часы, минуты и секунды
DELIMITER //

CREATE PROCEDURE FormatSeconds(IN seconds INT)
BEGIN
    DECLARE days INT;
    DECLARE hours INT;
    DECLARE minutes INT;
    DECLARE seconds_remainder INT;

    -- Вычисляем количество дней
    SET days = seconds DIV (24 * 60 * 60);
    SET seconds_remainder = seconds % (24 * 60 * 60);

    -- Вычисляем количество часов
    SET hours = seconds_remainder DIV (60 * 60);
    SET seconds_remainder = seconds_remainder % (60 * 60);

    -- Вычисляем количество минут
    SET minutes = seconds_remainder DIV 60;
    SET seconds_remainder = seconds_remainder % 60;

    -- Выводим результат
    SELECT CONCAT(days, ' days ', hours, ' hours ', minutes, ' minutes ', seconds_remainder, ' seconds');
END //

DELIMITER ;

-- Задание 2: Вывод четных чисел от 1 до 10
DELIMITER //

CREATE PROCEDURE PrintEvenNumbers()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 10 DO
        IF i % 2 = 0 THEN
            SELECT i;
        END IF;
        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

-- Задание 3: Создание процедуры для выбора пользователей по критериям
DELIMITER //

CREATE PROCEDURE SelectUsersForUser(IN userId INT)
BEGIN
    SELECT * FROM users WHERE id IN (
        SELECT DISTINCT target_user_id FROM friend_requests WHERE initiator_user_id = userId AND status = 'approved' LIMIT 5
        UNION
        SELECT DISTINCT initiator_user_id FROM friend_requests WHERE target_user_id = userId AND status = 'approved' LIMIT 5
    );
END //

DELIMITER ;

-- Задание 4: Создание функции для вычисления коэффициента популярности пользователя
DELIMITER //

CREATE FUNCTION CalculatePopularity(userId INT) RETURNS INT
BEGIN
    DECLARE friendCount INT;

    SELECT COUNT(*) INTO friendCount FROM friend_requests WHERE (initiator_user_id = userId OR target_user_id = userId) AND status = 'approved';

    RETURN friendCount;
END //

DELIMITER ;

-- Задание 5: Создание хранимой функции для приветствия в зависимости от времени суток
DELIMITER //

CREATE FUNCTION Hello() RETURNS VARCHAR(50)
BEGIN
    DECLARE greeting VARCHAR(50);
    DECLARE currentHour INT;

    SET currentHour = HOUR(NOW());

    IF currentHour >= 6 AND currentHour < 12 THEN
        SET greeting = 'Доброе утро';
    ELSEIF currentHour >= 12 AND currentHour < 18 THEN
        SET greeting = 'Добрый день';
    ELSEIF currentHour >= 18 AND currentHour < 24 THEN
        SET greeting = 'Добрый вечер';
    ELSE
        SET greeting = 'Доброй ночи';
    END IF;

    RETURN greeting;
END //

DELIMITER ;

-- Задание 6: Создание триггера для записи действий в таблицу логов
DELIMITER //

CREATE TRIGGER LogActions
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO logs (table_name, primary_key_id, action_time)
    VALUES ('users', NEW.id, NOW());
END;
//

CREATE TRIGGER LogActions2
AFTER INSERT ON communities
FOR EACH ROW
BEGIN
    INSERT INTO logs (table_name, primary_key_id, action_time)
    VALUES ('communities', NEW.id, NOW());
END;
//

CREATE TRIGGER LogActions3
AFTER INSERT ON messages
FOR EACH ROW
BEGIN
    INSERT INTO logs (table_name, primary_key_id, action_time)
    VALUES ('messages', NEW.id, NOW());
END;
//

DELIMITER ;

-- Запуск хранимой функции приветствия
SELECT Hello();