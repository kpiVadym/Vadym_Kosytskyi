# Selenium task
Selenium_kosytskyi.py - головний файл, де записано pipeline перевірки роботи заданого функціоналу сайту. 

**Кроки запуску**:
1) Завантажте браузер Chrome 
2) Завантажте selenium та webdriver_manager. 
Якщо у вас не втсановлено, то це можна зробити за допомгою команди pip у терміналі:
``` pip install selenium ```
``` pip install webdriver_manager ```

3) Запустіть Selenium_kosytskyi.py

**Можливі результати**: 
1) Якщо все успішно, то на консолі буде виведено повідомлення "Find. New job was added \n Find. New job was edited"
2) Інакше буде виведено одне з двох повідомлень: "Not find. New job was not added", "Not find. New job was not edited". Вони вкзаують на те, на якому етапі виникла помилка. 


