# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects APIs

"""


from pprint import pformat
from six import iteritems

class DiarizeSegment(object):

    def __init__(self, start=None, end=None, speaker_id=None):
        """
        DiarizeSegment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start': 'float',
            'end': 'float',
            'speaker_id': 'int'
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'speaker_id': 'speakerId'
        }

        self._start = start
        self._end = end
        self._speaker_id = speaker_id

    @property
    def start(self):
        """
        Gets the start of this DiarizeSegment.
        start of the corresponding diarized segment.

        :return: The encoding of this DiarizeSegment.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this DiarizeSegment.
        start of the corresponding diarized segment.

        :param start: The start of this DiarizeSegment.
        :type: float
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this DiarizeSegment.
        end of the corresponding diarized segment.

        :return: The end of this DiarizeSegment.
        :rtype: float
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this DiarizeSegment.
        end of the corresponding diarized segment.

        :param end: The end of this DiarizeSegment.
        :type: float
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")

        self._end = end

    @property
    def speaker_id(self):
        """
        Gets the speaker_id of this DiarizeSegment.
        Unique identifier of the speaker speaking in the segment

        :return: The speaker_id of this DiarizeSegment.
        :rtype: int
        """
        return self._speaker_id

    @speaker_id.setter
    def speaker_id(self, speaker_id):
        """
        Sets the speaker_id of this DiarizeSegment.
        Unique identifier of the speaker speaking in the segment

        :param speaker_id: The speaker_id of this DiarizeSegment.
        :type: sinttr
        """
        if speaker_id is None:
            raise ValueError("Invalid value for `speaker_id`, must not be `None`")

        self._speaker_id = speaker_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DiarizeSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
