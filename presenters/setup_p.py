from __future__ import annotations
from typing import Protocol
import os
from model.model import Model
from dotenv import load_dotenv


class View(Protocol):
    def init_setup_page_ui(self, presenter: SetupPresenter) -> None:
        ...

    def ask_user_for_api_key(self) -> str:
        ...
    
    def notyfy_key_update_state(self, state: bool) -> None:
        ...
    
    def update_openai_key_button_state(self, state: bool) -> None:
        ...

class SetupPresenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def handle_setup_page_ui_loading(self) -> None:
        self.view.init_setup_page_ui(self)
        self.handle_sp_buttons_states()

    def handle_sp_buttons_states(self) -> None:
        load_dotenv()
        self.view.update_openai_key_button_state(self.model.check_key_status_in_os())

    def handle_add_openai_key_button_click(self, event=None) -> None:
        key = self.view.ask_user_for_api_key()
        # Validate key
        key_state = self.model.validate_openai_api_key(key)
        # Store aquired key in .env if it is valid, if suceded then load key in nevironment
        if key_state and self.model.store_valid_key(key):
            self.handle_sp_buttons_states()
            self.view.notyfy_key_update_state(True)
        else:
            self.view.notyfy_key_update_state(False)

    def handle_select_openai_transcriber_button_click(self, event=None) -> None:
        # self.view.init_setup_page_ui(self)
        print("select open AI transcriber")

    def handle_select_alternative_transcriber_button_click(self, event=None) -> None:
        # self.view.init_setup_page_ui(self)
        print("select alternative!!!")

    def handle_phoneme_checkbox_clicked(self, event=None) -> None:
        # self.view.init_setup_page_ui(self)
        print("checkbox!!!")

        # # self.main_page_starter.config(command=presenter.handle_main_page_start_button_click)
        # self.openai_selector.config(command=presenter.handle_select_openai_transcriber_button_click)
        # self.openai_api_key_manager.config(command=presenter.handle_add_openai_key_button_click)
        # self.alternative_selector.config(command=presenter.handle_select_alternative_transcriber_button_click)
        # self.alternative_selector.config(command=presenter.handle_phoneme_checkbox_clicked)