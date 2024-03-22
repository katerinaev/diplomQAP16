from pages import MainPage


# def test_open_bot(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     main_page.click_on_bot_icon()
#
#     main_page.assert_that_chatbot_open()

def test_open_bot(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_bot_icon()

    main_page.assert_that_chatbot_open()


# def test_close_bot(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     main_page.click_on_bot()
#     main_page.close_alert()

