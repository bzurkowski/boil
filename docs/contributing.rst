Contribution guide
==================

Introduction
------------

Boil is a young project with great ambition for further development. So far, we have managed to build a framework for generic creation of project templates, as well as mechanisms for their automatic generation. We have several fully functional templates that demonstrate the tool's operation and are an invitation for the community to join the project and begin its expansion. These sample templates also pose a question to the community regarding the usefulness of the proposed solution to the problem.

In order to take full advantage of Boil's potential, the project must acquire versatility, which it does not have at the moment. To achieve this, community help is needed. No one, more than people in the community, knows better how to use technologies existing on the market. Ruby's specialist will provide the best templates for projects related to this language, the Ruby on Rails framework, building gems etc. Specialists from the Python community will help in building templates for the Django and Flask applications. Together with templates, these people can provide extremely valuable knowledge about good practices, design patterns, dependencies, naming conventions, documentation, security and many more.

If you are such a person and you are able to take a moment to share your expertise, thank you very much for your attention and cordially invite you to cooperate. This guide will show you how to contribute to the project and how to develop new categories of templates.

Developing plates
-----------------

Boil introduces an abstraction over project templates, which is called a "plate". Each plate consists of two elements:

**Template**

For dynamic generation of project files, Boil uses a commonly used template engine called Jinja. Each project file, eg README, is described using a separate Jinja template file, which, in addition to the content characteristic for a given file, may contain logical instructions (eg conditions), mathematical operations, list operations and dictionaries, inflection modifiers (eg string conversion to cemalcase or underscore). In addition, the engine has a configurable syntax, supports template inheritance and reuse of fragments through macros, is highly efficient and well documented. It is also recognizable in many communities, that's why many people will be able to apply for a contribution straight away without having to read the documentation.

**Python module**

