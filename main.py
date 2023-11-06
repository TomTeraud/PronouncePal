from model.model import Model
from view.main_view import MainView
from view.setup_view import SetupView
from presenters.setup_presenter import SetupPresenter
from presenters.main_presenter import MainPresenter
def main() -> None:
    model = Model()
    setup_v = SetupView()
    main_v = MainView()
    main_presenter = MainPresenter(model, main_v)
    setup_presenter = SetupPresenter(setup_v, main_presenter)

    setup_presenter.run()


if __name__ == "__main__":
    main()
