# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects APIs

"""


from pprint import pformat
from six import iteritems

class DiarizeAudio(object):

    def __init__(self, encoding=None, sample_rate=None, language_code='en-US', content=None, speakers=-1):
        """
        DiarizeAudio - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'encoding': 'str',
            'sample_rate': 'int',
            'language_code': 'str',
            'content': 'str',
            'speakers': 'int'
        }

        self.attribute_map = {
            'encoding': 'encoding',
            'sample_rate': 'sampleRate',
            'language_code': 'languageCode',
            'content': 'content',
            'speakers': 'speakers'
        }

        self._encoding = encoding
        self._sample_rate = sample_rate
        self._language_code = language_code
        self._content = content
        self._speakers = speakers

    @property
    def encoding(self):
        """
        Gets the encoding of this DiarizeAudio.
        Encoding of audio file like MP3, WAV etc.

        :return: The encoding of this DiarizeAudio.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this DiarizeAudio.
        Encoding of audio file like MP3, WAV etc.

        :param encoding: The encoding of this DiarizeAudio.
        :type: str
        """
        if encoding is None:
            raise ValueError("Invalid value for `encoding`, must not be `None`")

        self._encoding = encoding

    @property
    def sample_rate(self):
        """
        Gets the sample_rate of this DiarizeAudio.
        Sample rate of the audio file.

        :return: The sample_rate of this DiarizeAudio.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """
        Sets the sample_rate of this DiarizeAudio.
        Sample rate of the audio file.

        :param sample_rate: The sample_rate of this DiarizeAudio.
        :type: int
        """
        if sample_rate is None:
            raise ValueError("Invalid value for `sample_rate`, must not be `None`")

        self._sample_rate = sample_rate

    @property
    def language_code(self):
        """
        Gets the language_code of this DiarizeAudio.
        Language spoken in the audio file.

        :return: The language_code of this DiarizeAudio.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this DiarizeAudio.
        Language spoken in the audio file.

        :param language_code: The language_code of this DiarizeAudio.
        :type: str
        """
        if language_code is None:
            raise ValueError("Invalid value for `language_code`, must not be `None`")

        self._language_code = language_code

    @property
    def content(self):
        """
        Gets the content of this DiarizeAudio.
        base64 encoding of the audio file.

        :return: The content of this DiarizeAudio.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this DiarizeAudio.
        base64 encoding of the audio file.

        :param content: The content of this DiarizeAudio.
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

        self._content = content

    @property
    def speakers(self):
        """
        Gets the speakers of this DiarizeAudio.
        Number of speakers in the file (-1 for unknown speakers)

        :return: The speakers of this DiarizeAudio.
        :rtype: int
        """
        return self._speakers

    @speakers.setter
    def speakers(self, speakers):
        """
        Sets the speakers of this DiarizeAudio.
        Number of speakers in the file (-1 for unknown speakers)

        :param speakers: The speakers of this DiarizeAudio.
        :type: int
        """
        if speakers is None:
            raise ValueError("Invalid value for `speakers`, must not be `None`")

        self._speakers = speakers

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
        if not isinstance(other, DiarizeAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
