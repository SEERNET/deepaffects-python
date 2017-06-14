# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects audio APIs
"""


from pprint import pformat
from six import iteritems
import re


class EmotionScore(object):

    def __init__(self, emotion=None, score=None):
        """
        EmotionScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'emotion': 'str',
            'score': 'float'
        }

        self.attribute_map = {
            'emotion': 'emotion',
            'score': 'score'
        }

        self._emotion = emotion
        self._score = score

    @property
    def emotion(self):
        """
        Gets the emotion of this EmotionScore.
        Type of emotion like Happy, Sad, Surprised etc.

        :return: The emotion of this EmotionScore.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """
        Sets the emotion of this EmotionScore.
        Type of emotion like Happy, Sad, Surprised etc.

        :param emotion: The emotion of this EmotionScore.
        :type: str
        """
        if emotion is None:
            raise ValueError("Invalid value for `emotion`, must not be `None`")

        self._emotion = emotion

    @property
    def score(self):
        """
        Gets the score of this EmotionScore.
        Probability score or confidence of the corresponding emotion.

        :return: The score of this EmotionScore.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this EmotionScore.
        Probability score or confidence of the corresponding emotion.

        :param score: The score of this EmotionScore.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")

        self._score = score

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
        if not isinstance(other, EmotionScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
