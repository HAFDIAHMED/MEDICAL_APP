import shifaa.db.constants as csts
import shifaa.db.core as core
import shifaa.db.models as models


def get_faqs():
    with core.get_data_source().session() as sess:
        return sess.query(models.Faq).all()


def get_constants(name: str) -> models.JsonifiableCollection:
    for source, constants in csts.CONSTANTS.items():
        for element in constants:
            if element.get_name() == name:
                with core.get_data_source(source).session() as sess:
                    return models.JsonifiableCollection(
                        sess.query(
                            element.get_class_source()
                        )
                    )
