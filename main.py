from model.model import Model
from presenter.presenter import Presenter
from view.main_view import MainView
from view.setup_view import SetupView

def main() -> None:
    model = Model()
    setup_v = SetupView()
    main_v = MainView()
    presenter = Presenter(model, setup_v, main_v)
    presenter.run()


if __name__ == "__main__":
    main()
