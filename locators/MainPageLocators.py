from selenium.webdriver.common.by import By


class MainPageLocators:
    main_title = (By.TAG_NAME, "h1")
    no_tasks_li = (By.XPATH, "//li[contains(text(),'No tasks defined')]")
    new_task_div = (By.CLASS_NAME, "new-task-form")
    new_task_text_field = (By.ID, "new-task")
    new_task_submit = (By.CSS_SELECTOR, "input[type='submit']")
    task_list_items = (By.CLASS_NAME, "task")
    task_delete_button = (By.CLASS_NAME, "delete")
    reopen_specific_task_li = (By.CSS_SELECTOR, "")
    completed_lis = (By.CLASS_NAME, "task completed")
