from model.model import Model
from presenter.presenter import Presenter
from view.view import PronouncePal
from view.main_page import MainPageWidgets


def main() -> None:
    model = Model()
    view = PronouncePal()
    presenter = Presenter(model, view)
    presenter.run()


if __name__ == "__main__":
    main()
