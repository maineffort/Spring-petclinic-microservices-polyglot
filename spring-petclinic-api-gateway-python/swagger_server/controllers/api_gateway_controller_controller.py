import connexion
import six

from swagger_server.models.owner_details import OwnerDetails  # noqa: E501
from swagger_server import util


def get_owner_details_using_get(ownerId):  # noqa: E501
    """getOwnerDetails

     # noqa: E501

    :param ownerId: ownerId
    :type ownerId: int

    :rtype: OwnerDetails
    """
    return 'do some magic!'
