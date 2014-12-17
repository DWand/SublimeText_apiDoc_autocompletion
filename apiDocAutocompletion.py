# Sublime Text Plugin
# apiDocAutocompletion adds apiDoc tags to list of code completion suggestions.
# Project: https://github.com/DWand/SublimeText_apiDoc_autocompletion
# License: MIT

import sublime
import sublime_plugin

class apiDocAutocompletion(sublime_plugin.EventListener):
    _suggestions = [
        ("@api\tapiDoc", "@api {${1:method}} ${2:path} ${3:[title]}"),
        ("@apiDefine\tapiDoc", "@apiDefine ${1:name} ${2:[title]}\n${3:* }           ${4:[description]}"),
        ("@apiDescription\tapiDoc", "@apiDescription ${1:text}"),
        ("@apiError\tapiDoc", "@apiError ${1:[(group)]} ${2:[{type\}]} ${3:field} ${4:[description]}"),
        ("@apiErrorExample\tapiDoc", "@apiErrorExample ${1:[{type\}]} ${2:[title]}\n${3:* }${4:example}"),
        ("@apiExample\tapiDoc", "@apiExample ${1:[{type\}]} ${2:title}\n${3:* }${4:example}"),
        ("@apiGroup\tapiDoc", "@apiGroup ${1:name}"),
        ("@apiHeader\tapiDoc", "@apiHeader ${1:[(group)]} ${2:[{type\}]} ${3:[field=defaultValue]} ${4:[description]}"),
        ("@apiHeaderExample\tapiDoc", "@apiHeaderExample ${1:[{type\}]} ${2:[title]}\n${3:* }${4:example}"),
        ("@apiIgnore\tapiDoc", "@apiIgnore ${1:[hint]}"),
        ("@apiName\tapiDoc", "@apiName ${1:name}"),
        ("@apiParam\tapiDoc", "@apiParam ${1:[(group)]} ${2:[{type\}]} ${3:[field=defaultValue]} ${4:[description]}"),
        ("@apiParamExample\tapiDoc", "@apiParamExample ${1:[{type\}]} ${2:[title]}\n${3:* }${4:example}"),
        ("@apiPermission\tapiDoc", "@apiPermission ${1:name}"),
        ("@apiSampleRequest\tapiDoc", "@apiSampleRequest ${1:url}"),
        ("@apiSuccess\tapiDoc", "@apiSuccess ${1:[(group)]} ${2:[{type\}]} ${3:field} ${4:[description]}"),
        ("@apiSuccessExample\tapiDoc", "@apiSuccessExample ${1:[{type\}]} ${2:[title]}\n${3:* }${4:example}"),
        ("@apiUse\tapiDoc", "@apiUse ${1:name}"),
        ("@apiVersion\tapiDoc", "@apiVersion ${1:version}"),
        ("@apiDefineErrorStructure\tapiDoc [deprecated]", "@apiDefineErrorStructure ${1:name}"),
        ("@apiDefineHeaderStructure\tapiDoc [deprecated]", "@apiDefineHeaderStructure ${1:name}"),
        ("@apiDefinePermission\tapiDoc [deprecated]", "@apiDefinePermission ${1:name} ${2:[title]}\n${3:* }                     ${4:[description]}"),
        ("@apiDefineStructure\tapiDoc [deprecated]", "@apiDefineStructure ${1:name}"),
        ("@apiDefineSuccessStructure\tapiDoc [deprecated]", "@apiDefineSuccessStructure ${1:name}"),
        ("@apiErrorStructure\tapiDoc [deprecated]", "@apiErrorStructure ${1:name}"),
        ("@apiErrorTitle\tapiDoc [deprecated]", "@apiErrorTitle (${1:group}) ${2:description}"),
        ("@apiGroupDescription\tapiDoc [deprecated]", "@apiGroupDescription ${1:text}"),
        ("@apiHeaderStructure\tapiDoc [deprecated]", "@apiHeaderStructure ${1:name}"),
        ("@apiHeaderTitle\tapiDoc [deprecated]", "@apiHeaderTitle (${1:group}) ${2:description}"),
        ("@apiParamTitle\tapiDoc [deprecated]", "@apiParamTitle (${1:group}) ${2:description}"),
        ("@apiStructure\tapiDoc [deprecated]", "@apiStructure ${1:name}"),
        ("@apiSuccessStructure\tapiDoc [deprecated]", "@apiSuccessStructure ${1:name}"),
        ("@apiSuccessTitle\tapiDoc [deprecated]", "@apiSuccessTitle (${1:group}) ${2:description}"),
    ]

    def on_query_completions(self, view, prefix, locations):
        
        # Block comment scopes:
        # C#:
        #     source.cs comment.block.source.cs
        # Go:
        #     source.go comment.block.go
        # Dart:
        #     -
        # Java:
        #     source.java comment.block.documentation.javadoc meta.documentation.comment.javadoc text.html
        # JavaScript:
        #     source.js comment.block.documentation.js
        # PHP:
        #     text.html.basic source.php.embedded.block.html comment.block.documentation.phpdoc.php
        # CoffeeScript:
        #     source.coffee comment.block.coffee
        # Erlang:
        #     source.erlang
        # Perl:
        #     source.perl meta.comment.full-line.perl comment.line.number-sign.perl
        #     source.perl comment.block.documentation.perl
        # Python:
        #     source.python string.quoted.double.block.python
        # Ruby:
        #     source.ruby comment.block.documentation.ruby
        
        target_scopes = [
            "comment.block",
            "source.perl meta.comment.full-line.perl comment.line.number-sign.perl",
            "source.python string.quoted.double.block.python",
            "source.erlang"
        ]

        location = locations[0]
        current_scope = view.scope_name(location)

        if any(scope in current_scope for scope in target_scopes) == True:
            return apiDocAutocompletion._suggestions
        else:
            return []