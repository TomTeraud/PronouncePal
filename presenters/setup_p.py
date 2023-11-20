from __future__ import annotations
from typing import Protocol
from model.model import Model

from model.setup_page_button_controller import SetupPageButtonController as SPBC


class View(Protocol):
    def init_setup_page_ui(self, presenter: SetupPresenter) -> None:
        ...

    def ask_user_for_api_key(self) -> str:
        ...
    
    def notify_key_update_state(self, state: bool) -> None:
        ...
    
    def update_openai_key_button_state(self, state: bool) -> None:
        ...
    
    def update_openai_selector_button_state(self, state: bool) -> None:
        ...
    
    def update_alternative_selector_button_state(self, state: bool) -> None:
        ...
    
    def update_app_start_button_state(self, state: bool) -> None:
        ...

    def update_check_box_state(self, state: bool) -> None:
        ...

class SetupPresenter:
    def __init__(self, model: Model, view: View, s_p_b_ctrl: SPBC):
        self.model = model
        self.view = view
        self.s_p_b_ctrl = s_p_b_ctrl

    def handle_setup_page_ui_loading(self) -> None:
        self.view.init_setup_page_ui(self)
        self.update_setup_buttons()

    def update_setup_buttons(self) -> None:
        self.view.update_openai_key_button_state(self.s_p_b_ctrl.get_openai_api_key_button_state())
        self.view.update_openai_selector_button_state(self.s_p_b_ctrl.get_openai_selector_button_state())
        self.view.update_alternative_selector_button_state(self.s_p_b_ctrl.get_alternative_selector_button_state())
        self.view.update_app_start_button_state(self.s_p_b_ctrl.get_app_start_button_state())

    def handle_add_openai_key_button_click(self, event=None) -> None:
        key = self.view.ask_user_for_api_key()
        # Validate key
        key_state = self.model.validate_openai_api_key(key)
        # Store aquired key in .env if it is valid, if suceded then load key in nevironment
        if key_state and self.model.store_valid_key(key):
            self.view.notify_key_update_state(True)
        else:
            self.view.notify_key_update_state(False)
        self.update_setup_buttons()

    def handle_select_openai_transcriber_button_click(self, event=None) -> None:
        self.s_p_b_ctrl.select_openai_triggered()
        self.update_setup_buttons()

    def handle_select_alternative_transcriber_button_click(self, event=None) -> None:
        self.s_p_b_ctrl.select_alternative_triggered()
        self.update_setup_buttons()

    def handle_phoneme_checkbox_clicked(self, event=None) -> None:
        state = self.model.handle_phoneme_checkbox_click()
        self.view.update_check_box_state(state)
