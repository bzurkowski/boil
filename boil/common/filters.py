import inflection


camelize = inflection.camelize
underscore = inflection.underscore
dasherize = inflection.dasherize
humanize = inflection.humanize
titleize = inflection.titleize
parameterize = inflection.parameterize
pluralize = inflection.pluralize
singularize = inflection.singularize
ordinal = inflection.ordinal
ordinalize = inflection.ordinalize


PLATE_FILTERS = {
    'camelize': camelize,
    'underscore': underscore,
    'dasherize': dasherize,
    'humanize': humanize,
    'titleize': titleize,
    'parameterize': parameterize,
    'pluralize': pluralize,
    'singularize': singularize,
    'ordinal': ordinal,
    'ordinalize': ordinalize
}
