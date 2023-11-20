from model.model import Model
from presenters.presenters import Presenters
from view.views import Views



def main():
    model = Model()
    views = Views()
    presenters = Presenters(model, views)

    presenters.run()


if __name__ == "__main__":
    main()
