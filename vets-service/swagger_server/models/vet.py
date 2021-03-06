# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.specialty import Specialty  # noqa: F401,E501
from swagger_server import util


class Vet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, first_name: str=None, id: int=None, last_name: str=None, nr_of_specialties: int=None, specialties: List[Specialty]=None):  # noqa: E501
        """Vet - a model defined in Swagger

        :param first_name: The first_name of this Vet.  # noqa: E501
        :type first_name: str
        :param id: The id of this Vet.  # noqa: E501
        :type id: int
        :param last_name: The last_name of this Vet.  # noqa: E501
        :type last_name: str
        :param nr_of_specialties: The nr_of_specialties of this Vet.  # noqa: E501
        :type nr_of_specialties: int
        :param specialties: The specialties of this Vet.  # noqa: E501
        :type specialties: List[Specialty]
        """
        self.swagger_types = {
            'first_name': str,
            'id': int,
            'last_name': str,
            'nr_of_specialties': int,
            'specialties': List[Specialty]
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'id': 'id',
            'last_name': 'lastName',
            'nr_of_specialties': 'nrOfSpecialties',
            'specialties': 'specialties'
        }

        self._first_name = first_name
        self._id = id
        self._last_name = last_name
        self._nr_of_specialties = nr_of_specialties
        self._specialties = specialties

    @classmethod
    def from_dict(cls, dikt) -> 'Vet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Vet of this Vet.  # noqa: E501
        :rtype: Vet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Vet.


        :return: The first_name of this Vet.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Vet.


        :param first_name: The first_name of this Vet.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def id(self) -> int:
        """Gets the id of this Vet.


        :return: The id of this Vet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Vet.


        :param id: The id of this Vet.
        :type id: int
        """

        self._id = id

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Vet.


        :return: The last_name of this Vet.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Vet.


        :param last_name: The last_name of this Vet.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def nr_of_specialties(self) -> int:
        """Gets the nr_of_specialties of this Vet.


        :return: The nr_of_specialties of this Vet.
        :rtype: int
        """
        return self._nr_of_specialties

    @nr_of_specialties.setter
    def nr_of_specialties(self, nr_of_specialties: int):
        """Sets the nr_of_specialties of this Vet.


        :param nr_of_specialties: The nr_of_specialties of this Vet.
        :type nr_of_specialties: int
        """

        self._nr_of_specialties = nr_of_specialties

    @property
    def specialties(self) -> List[Specialty]:
        """Gets the specialties of this Vet.


        :return: The specialties of this Vet.
        :rtype: List[Specialty]
        """
        return self._specialties

    @specialties.setter
    def specialties(self, specialties: List[Specialty]):
        """Sets the specialties of this Vet.


        :param specialties: The specialties of this Vet.
        :type specialties: List[Specialty]
        """

        self._specialties = specialties
