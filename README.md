# Проект автоматизации тестирования API сервиса Яндекс.Самокат

1. Ссылка на сервис: "https://qa-scooter.praktikum-services.ru"
2. Основа для написания автотестов — модуль request
3. Установить зависимости — pip install -r requirements.txt 
4. Проверить, что request,json, pytest, allure, faker установлены: pip freeze
5. Команда для запуска — run
7. Генерация данных курьера, удаление курьера – в файле conftest.generating_the_cour_and_delete_the_cour().
8. Генерация данных заказа - в файле helpers.fake_data_order().
8. Запустить allure отчет: allure serve allure_results