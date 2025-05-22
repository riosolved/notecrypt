from abc import ABC, abstractmethod

class Mailer(ABC):
    @abstractmethod
    def email(self, to, subject, body):
        pass

    # TODO
    @abstractmethod
    def close():
        pass