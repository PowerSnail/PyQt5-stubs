# The PEP 484 type hints stub file for the QtXml module.
#
# Generated by SIP 6.0.3
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt5.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

from PyQt5 import sip

from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QDomImplementation(sip.simplewrapper):

    class InvalidDataPolicy(int):
        AcceptInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        DropInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        ReturnNullNode = ... # type: QDomImplementation.InvalidDataPolicy

    AcceptInvalidChars = ...  # type: QDomImplementation.InvalidDataPolicy
    DropInvalidChars = ...  # type: QDomImplementation.InvalidDataPolicy
    ReturnNullNode = ...  # type: QDomImplementation.InvalidDataPolicy

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomImplementation') -> None: ...

    def isNull(self) -> bool: ...
    @staticmethod
    def setInvalidDataPolicy(policy: 'QDomImplementation.InvalidDataPolicy') -> None: ...
    @staticmethod
    def invalidDataPolicy() -> 'QDomImplementation.InvalidDataPolicy': ...
    def createDocument(self, nsURI: str, qName: str, doctype: 'QDomDocumentType') -> 'QDomDocument': ...
    def createDocumentType(self, qName: str, publicId: str, systemId: str) -> 'QDomDocumentType': ...
    def hasFeature(self, feature: str, version: str) -> bool: ...


class QDomNode(sip.simplewrapper):

    class EncodingPolicy(int):
        EncodingFromDocument = ... # type: QDomNode.EncodingPolicy
        EncodingFromTextStream = ... # type: QDomNode.EncodingPolicy

    EncodingFromDocument = ...  # type: QDomNode.EncodingPolicy
    EncodingFromTextStream = ...  # type: QDomNode.EncodingPolicy

    class NodeType(int):
        ElementNode = ... # type: QDomNode.NodeType
        AttributeNode = ... # type: QDomNode.NodeType
        TextNode = ... # type: QDomNode.NodeType
        CDATASectionNode = ... # type: QDomNode.NodeType
        EntityReferenceNode = ... # type: QDomNode.NodeType
        EntityNode = ... # type: QDomNode.NodeType
        ProcessingInstructionNode = ... # type: QDomNode.NodeType
        CommentNode = ... # type: QDomNode.NodeType
        DocumentNode = ... # type: QDomNode.NodeType
        DocumentTypeNode = ... # type: QDomNode.NodeType
        DocumentFragmentNode = ... # type: QDomNode.NodeType
        NotationNode = ... # type: QDomNode.NodeType
        BaseNode = ... # type: QDomNode.NodeType
        CharacterDataNode = ... # type: QDomNode.NodeType

    ElementNode = ...  # type: QDomNode.NodeType
    AttributeNode = ...  # type: QDomNode.NodeType
    TextNode = ...  # type: QDomNode.NodeType
    CDATASectionNode = ...  # type: QDomNode.NodeType
    EntityReferenceNode = ...  # type: QDomNode.NodeType
    EntityNode = ...  # type: QDomNode.NodeType
    ProcessingInstructionNode = ...  # type: QDomNode.NodeType
    CommentNode = ...  # type: QDomNode.NodeType
    DocumentNode = ...  # type: QDomNode.NodeType
    DocumentTypeNode = ...  # type: QDomNode.NodeType
    DocumentFragmentNode = ...  # type: QDomNode.NodeType
    NotationNode = ...  # type: QDomNode.NodeType
    BaseNode = ...  # type: QDomNode.NodeType
    CharacterDataNode = ...  # type: QDomNode.NodeType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNode') -> None: ...

    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def nextSiblingElement(self, taName: str = ...) -> 'QDomElement': ...
    def previousSiblingElement(self, tagName: str = ...) -> 'QDomElement': ...
    def lastChildElement(self, tagName: str = ...) -> 'QDomElement': ...
    def firstChildElement(self, tagName: str = ...) -> 'QDomElement': ...
    def save(self, a0: QtCore.QTextStream, a1: int, a2: 'QDomNode.EncodingPolicy' = ...) -> None: ...
    def toComment(self) -> 'QDomComment': ...
    def toCharacterData(self) -> 'QDomCharacterData': ...
    def toProcessingInstruction(self) -> 'QDomProcessingInstruction': ...
    def toNotation(self) -> 'QDomNotation': ...
    def toEntity(self) -> 'QDomEntity': ...
    def toText(self) -> 'QDomText': ...
    def toEntityReference(self) -> 'QDomEntityReference': ...
    def toElement(self) -> 'QDomElement': ...
    def toDocumentType(self) -> 'QDomDocumentType': ...
    def toDocument(self) -> 'QDomDocument': ...
    def toDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def toCDATASection(self) -> 'QDomCDATASection': ...
    def toAttr(self) -> 'QDomAttr': ...
    def clear(self) -> None: ...
    def isNull(self) -> bool: ...
    def namedItem(self, name: str) -> 'QDomNode': ...
    def isComment(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isText(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isAttr(self) -> bool: ...
    def setPrefix(self, pre: str) -> None: ...
    def prefix(self) -> str: ...
    def setNodeValue(self, a0: str) -> None: ...
    def nodeValue(self) -> str: ...
    def hasAttributes(self) -> bool: ...
    def localName(self) -> str: ...
    def namespaceURI(self) -> str: ...
    def ownerDocument(self) -> 'QDomDocument': ...
    def attributes(self) -> 'QDomNamedNodeMap': ...
    def nextSibling(self) -> 'QDomNode': ...
    def previousSibling(self) -> 'QDomNode': ...
    def lastChild(self) -> 'QDomNode': ...
    def firstChild(self) -> 'QDomNode': ...
    def childNodes(self) -> 'QDomNodeList': ...
    def parentNode(self) -> 'QDomNode': ...
    def nodeType(self) -> 'QDomNode.NodeType': ...
    def nodeName(self) -> str: ...
    def isSupported(self, feature: str, version: str) -> bool: ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep: bool = ...) -> 'QDomNode': ...
    def hasChildNodes(self) -> bool: ...
    def appendChild(self, newChild: 'QDomNode') -> 'QDomNode': ...
    def removeChild(self, oldChild: 'QDomNode') -> 'QDomNode': ...
    def replaceChild(self, newChild: 'QDomNode', oldChild: 'QDomNode') -> 'QDomNode': ...
    def insertAfter(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...
    def insertBefore(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...


class QDomNodeList(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNodeList') -> None: ...

    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def at(self, index: int) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...


class QDomDocumentType(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentType') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def internalSubset(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...
    def notations(self) -> 'QDomNamedNodeMap': ...
    def entities(self) -> 'QDomNamedNodeMap': ...
    def name(self) -> str: ...


class QDomDocument(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, doctype: QDomDocumentType) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocument') -> None: ...

    def toByteArray(self, indent: int = ...) -> QtCore.QByteArray: ...
    def toString(self, indent: int = ...) -> str: ...
    @typing.overload
    def setContent(self, text: typing.Union[QtCore.QByteArray, bytes, bytearray], namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: str, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, dev: QtCore.QIODevice, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, source: 'QXmlInputSource', namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: str) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, dev: QtCore.QIODevice) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, source: 'QXmlInputSource', reader: 'QXmlReader') -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, reader: QtCore.QXmlStreamReader, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def documentElement(self) -> 'QDomElement': ...
    def implementation(self) -> QDomImplementation: ...
    def doctype(self) -> QDomDocumentType: ...
    def elementById(self, elementId: str) -> 'QDomElement': ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def createAttributeNS(self, nsURI: str, qName: str) -> 'QDomAttr': ...
    def createElementNS(self, nsURI: str, qName: str) -> 'QDomElement': ...
    def importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def createEntityReference(self, name: str) -> 'QDomEntityReference': ...
    def createAttribute(self, name: str) -> 'QDomAttr': ...
    def createProcessingInstruction(self, target: str, data: str) -> 'QDomProcessingInstruction': ...
    def createCDATASection(self, data: str) -> 'QDomCDATASection': ...
    def createComment(self, data: str) -> 'QDomComment': ...
    def createTextNode(self, data: str) -> 'QDomText': ...
    def createDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def createElement(self, tagName: str) -> 'QDomElement': ...


class QDomNamedNodeMap(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNamedNodeMap') -> None: ...

    def contains(self, name: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def removeNamedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def setNamedItemNS(self, newNode: QDomNode) -> QDomNode: ...
    def namedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...
    def removeNamedItem(self, name: str) -> QDomNode: ...
    def setNamedItem(self, newNode: QDomNode) -> QDomNode: ...
    def namedItem(self, name: str) -> QDomNode: ...


class QDomDocumentFragment(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentFragment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCharacterData(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCharacterData') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, a0: str) -> None: ...
    def data(self) -> str: ...
    def length(self) -> int: ...
    def replaceData(self, offset: int, count: int, arg: str) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def insertData(self, offset: int, arg: str) -> None: ...
    def appendData(self, arg: str) -> None: ...
    def substringData(self, offset: int, count: int) -> str: ...


class QDomAttr(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomAttr') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setValue(self, a0: str) -> None: ...
    def value(self) -> str: ...
    def ownerElement(self) -> 'QDomElement': ...
    def specified(self) -> bool: ...
    def name(self) -> str: ...


class QDomElement(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomElement') -> None: ...

    def text(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def attributes(self) -> QDomNamedNodeMap: ...
    def setTagName(self, name: str) -> None: ...
    def tagName(self) -> str: ...
    def hasAttributeNS(self, nsURI: str, localName: str) -> bool: ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNodeNS(self, nsURI: str, localName: str) -> QDomAttr: ...
    def removeAttributeNS(self, nsURI: str, localName: str) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: str, qName: str, value: str) -> None: ...
    @typing.overload
    # def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None: ...
    # @typing.overload
    # def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None: ...
    # @typing.overload
    def setAttributeNS(self, nsURI: str, qName: str, value: float) -> None: ...
    # @typing.overload
    # def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None: ...
    def attributeNS(self, nsURI: str, localName: str, defaultValue: str = ...) -> str: ...
    def hasAttribute(self, name: str) -> bool: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr: ...
    def setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNode(self, name: str) -> QDomAttr: ...
    def removeAttribute(self, name: str) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: str) -> None: ...
    @typing.overload
    # def setAttribute(self, name: str, value: int) -> None: ...
    # @typing.overload
    # def setAttribute(self, name: str, value: int) -> None: ...
    # @typing.overload
    def setAttribute(self, name: str, value: float) -> None: ...
    # @typing.overload
    # def setAttribute(self, name: str, value: int) -> None: ...
    def attribute(self, name: str, defaultValue: str = ...) -> str: ...


class QDomText(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomText') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def splitText(self, offset: int) -> 'QDomText': ...


class QDomComment(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomComment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCDATASection(QDomText):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCDATASection') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomNotation(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomNotation') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntity(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntity') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntityReference(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntityReference') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomProcessingInstruction(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomProcessingInstruction') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, d: str) -> None: ...
    def data(self) -> str: ...
    def target(self) -> str: ...


class QXmlNamespaceSupport(sip.simplewrapper):

    def __init__(self) -> None: ...

    def reset(self) -> None: ...
    def popContext(self) -> None: ...
    def pushContext(self) -> None: ...
    @typing.overload
    def prefixes(self) -> typing.List[str]: ...
    @typing.overload
    def prefixes(self, a0: str) -> typing.List[str]: ...
    def processName(self, a0: str, a1: bool, a2: str, a3: str) -> None: ...
    def splitName(self, a0: str, a1: str, a2: str) -> None: ...
    def uri(self, a0: str) -> str: ...
    def prefix(self, a0: str) -> str: ...
    def setPrefix(self, a0: str, a1: str) -> None: ...


class QXmlAttributes(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlAttributes') -> None: ...

    def swap(self, other: 'QXmlAttributes') -> None: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def append(self, qName: str, uri: str, localPart: str, value: str) -> None: ...
    def clear(self) -> None: ...
    @typing.overload
    def value(self, index: int) -> str: ...
    @typing.overload
    def value(self, qName: str) -> str: ...
    @typing.overload
    def value(self, uri: str, localName: str) -> str: ...
    @typing.overload
    def type(self, index: int) -> str: ...
    @typing.overload
    def type(self, qName: str) -> str: ...
    @typing.overload
    def type(self, uri: str, localName: str) -> str: ...
    def uri(self, index: int) -> str: ...
    def qName(self, index: int) -> str: ...
    def localName(self, index: int) -> str: ...
    def length(self) -> int: ...
    @typing.overload
    def index(self, qName: str) -> int: ...
    @typing.overload
    def index(self, uri: str, localPart: str) -> int: ...


class QXmlInputSource(sip.simplewrapper):

    EndOfData = ... # type: int
    EndOfDocument = ... # type: int

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, dev: QtCore.QIODevice) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlInputSource') -> None: ...

    def fromRawData(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], beginning: bool = ...) -> str: ...
    def reset(self) -> None: ...
    def next(self) -> str: ...
    def data(self) -> str: ...
    def fetchData(self) -> None: ...
    @typing.overload
    def setData(self, dat: str) -> None: ...
    @typing.overload
    def setData(self, dat: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...


class QXmlParseException(sip.simplewrapper):

    @typing.overload
    def __init__(self, name: str = ..., column: int = ..., line: int = ..., publicId: str = ..., systemId: str = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QXmlParseException') -> None: ...

    def message(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...
    def lineNumber(self) -> int: ...
    def columnNumber(self) -> int: ...


class QXmlReader(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlReader') -> None: ...

    # @typing.overload
    # def parse(self, input: QXmlInputSource) -> bool: ...
    # @typing.overload
    def parse(self, input: QXmlInputSource) -> bool: ...
    def declHandler(self) -> 'QXmlDeclHandler': ...
    def setDeclHandler(self, handler: 'QXmlDeclHandler') -> None: ...
    def lexicalHandler(self) -> 'QXmlLexicalHandler': ...
    def setLexicalHandler(self, handler: 'QXmlLexicalHandler') -> None: ...
    def errorHandler(self) -> 'QXmlErrorHandler': ...
    def setErrorHandler(self, handler: 'QXmlErrorHandler') -> None: ...
    def contentHandler(self) -> 'QXmlContentHandler': ...
    def setContentHandler(self, handler: 'QXmlContentHandler') -> None: ...
    def DTDHandler(self) -> 'QXmlDTDHandler': ...
    def setDTDHandler(self, handler: 'QXmlDTDHandler') -> None: ...
    def entityResolver(self) -> 'QXmlEntityResolver': ...
    def setEntityResolver(self, handler: 'QXmlEntityResolver') -> None: ...
    def hasProperty(self, name: str) -> bool: ...
    def setProperty(self, name: str, value: sip.voidptr) -> None: ...
    def property(self, name: str) -> typing.Tuple[sip.voidptr, bool]: ...
    def hasFeature(self, name: str) -> bool: ...
    def setFeature(self, name: str, value: bool) -> None: ...
    def feature(self, name: str) -> typing.Tuple[bool, bool]: ...


class QXmlSimpleReader(QXmlReader):

    def __init__(self) -> None: ...

    def parseContinue(self) -> bool: ...
    @typing.overload
    def parse(self, input: QXmlInputSource) -> bool: ...
    @typing.overload
    def parse(self, input: QXmlInputSource, incremental: bool) -> bool: ...
    def declHandler(self) -> 'QXmlDeclHandler': ...
    def setDeclHandler(self, handler: 'QXmlDeclHandler') -> None: ...
    def lexicalHandler(self) -> 'QXmlLexicalHandler': ...
    def setLexicalHandler(self, handler: 'QXmlLexicalHandler') -> None: ...
    def errorHandler(self) -> 'QXmlErrorHandler': ...
    def setErrorHandler(self, handler: 'QXmlErrorHandler') -> None: ...
    def contentHandler(self) -> 'QXmlContentHandler': ...
    def setContentHandler(self, handler: 'QXmlContentHandler') -> None: ...
    def DTDHandler(self) -> 'QXmlDTDHandler': ...
    def setDTDHandler(self, handler: 'QXmlDTDHandler') -> None: ...
    def entityResolver(self) -> 'QXmlEntityResolver': ...
    def setEntityResolver(self, handler: 'QXmlEntityResolver') -> None: ...
    def hasProperty(self, name: str) -> bool: ...
    def setProperty(self, name: str, value: sip.voidptr) -> None: ...
    def property(self, name: str) -> typing.Tuple[sip.voidptr, bool]: ...
    def hasFeature(self, name: str) -> bool: ...
    def setFeature(self, name: str, value: bool) -> None: ...
    def feature(self, name: str) -> typing.Tuple[bool, bool]: ...


class QXmlLocator(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlLocator') -> None: ...

    def lineNumber(self) -> int: ...
    def columnNumber(self) -> int: ...


class QXmlContentHandler(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlContentHandler') -> None: ...

    def errorString(self) -> str: ...
    def skippedEntity(self, name: str) -> bool: ...
    def processingInstruction(self, target: str, data: str) -> bool: ...
    def ignorableWhitespace(self, ch: str) -> bool: ...
    def characters(self, ch: str) -> bool: ...
    def endElement(self, namespaceURI: str, localName: str, qName: str) -> bool: ...
    def startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool: ...
    def endPrefixMapping(self, prefix: str) -> bool: ...
    def startPrefixMapping(self, prefix: str, uri: str) -> bool: ...
    def endDocument(self) -> bool: ...
    def startDocument(self) -> bool: ...
    def setDocumentLocator(self, locator: QXmlLocator) -> None: ...


class QXmlErrorHandler(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlErrorHandler') -> None: ...

    def errorString(self) -> str: ...
    def fatalError(self, exception: QXmlParseException) -> bool: ...
    def error(self, exception: QXmlParseException) -> bool: ...
    def warning(self, exception: QXmlParseException) -> bool: ...


class QXmlDTDHandler(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlDTDHandler') -> None: ...

    def errorString(self) -> str: ...
    def unparsedEntityDecl(self, name: str, publicId: str, systemId: str, notationName: str) -> bool: ...
    def notationDecl(self, name: str, publicId: str, systemId: str) -> bool: ...


class QXmlEntityResolver(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlEntityResolver') -> None: ...

    def errorString(self) -> str: ...
    def resolveEntity(self, publicId: str, systemId: str) -> typing.Tuple[bool, QXmlInputSource]: ...


class QXmlLexicalHandler(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlLexicalHandler') -> None: ...

    def errorString(self) -> str: ...
    def comment(self, ch: str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def startCDATA(self) -> bool: ...
    def endEntity(self, name: str) -> bool: ...
    def startEntity(self, name: str) -> bool: ...
    def endDTD(self) -> bool: ...
    def startDTD(self, name: str, publicId: str, systemId: str) -> bool: ...


class QXmlDeclHandler(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlDeclHandler') -> None: ...

    def errorString(self) -> str: ...
    def externalEntityDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def internalEntityDecl(self, name: str, value: str) -> bool: ...
    def attributeDecl(self, eName: str, aName: str, type: str, valueDefault: str, value: str) -> bool: ...


class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):

    def __init__(self) -> None: ...

    def errorString(self) -> str: ...
    def externalEntityDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def internalEntityDecl(self, name: str, value: str) -> bool: ...
    def attributeDecl(self, eName: str, aName: str, type: str, valueDefault: str, value: str) -> bool: ...
    def comment(self, ch: str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def startCDATA(self) -> bool: ...
    def endEntity(self, name: str) -> bool: ...
    def startEntity(self, name: str) -> bool: ...
    def endDTD(self) -> bool: ...
    def startDTD(self, name: str, publicId: str, systemId: str) -> bool: ...
    def resolveEntity(self, publicId: str, systemId: str) -> typing.Tuple[bool, QXmlInputSource]: ...
    def unparsedEntityDecl(self, name: str, publicId: str, systemId: str, notationName: str) -> bool: ...
    def notationDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def fatalError(self, exception: QXmlParseException) -> bool: ...
    def error(self, exception: QXmlParseException) -> bool: ...
    def warning(self, exception: QXmlParseException) -> bool: ...
    def skippedEntity(self, name: str) -> bool: ...
    def processingInstruction(self, target: str, data: str) -> bool: ...
    def ignorableWhitespace(self, ch: str) -> bool: ...
    def characters(self, ch: str) -> bool: ...
    def endElement(self, namespaceURI: str, localName: str, qName: str) -> bool: ...
    def startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool: ...
    def endPrefixMapping(self, prefix: str) -> bool: ...
    def startPrefixMapping(self, prefix: str, uri: str) -> bool: ...
    def endDocument(self) -> bool: ...
    def startDocument(self) -> bool: ...
    def setDocumentLocator(self, locator: QXmlLocator) -> None: ...
