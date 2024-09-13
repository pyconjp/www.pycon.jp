from myst_parser.mdit_to_docutils import base

def setup(app):
    # refs: https://github.com/executablebooks/MyST-Parser/issues/760
    base.escapeHtml = lambda s: s

    return {
        'version': '0.1',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
