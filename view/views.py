from view.main_page.main_v import MainView
from view.menu_bar.mbv_master import MenuBarView
from view.setup_page.setup_v import SetupView
from view.helpers.view_custom_fun import column_row_configure


class Views(MenuBarView, SetupView, MainView):
    def __init__(self):
        super().__init__()
        
    def init_main_page_ui(self, presenter) -> None:
        self.destroy_frames_widgets()
        column_row_configure(self.mainframe, 1, 2)
        self.create_main_widgets(presenter)

    def init_setup_page_ui(self, presenter) -> None:
        self.destroy_frames_widgets()
        column_row_configure(self.mainframe, 2, 6)
        self.create_setup_widgets(presenter)

    def destroy_frames_widgets(self) -> None:
        widgets = self.mainframe.winfo_children()

        # Loop through the widgets and destroy each one
        for widget in widgets:
            widget.destroy()
