from django_assets import Bundle, register

common_css = Bundle(
    'sass/bootstrap/bootstrap.scss',
    'sass/cmsbootstrap.scss',
    filters='pyscss, cssmin',
    output='css/cmsbootstrap/common.min.css',
    depends=['sass/bootstrap/*.scss', 'sass/*.scss'])

register('cmsbootstrap.common_css', common_css)

common_js = Bundle(
    'cmsbootstrap/ie_version.js',
    filters='jsmin',
    output='js/cmsbootstrap/common.min.js'
    )

register('cmsbootstrap.common_js', common_js)

ie8_js = Bundle(
    'cmsbootstrap/html5shiv.js',
    'cmsbootstrap/respond.min.js',
    filters='jsmin',
    output='js/cmsbootstrap/ie8.min.js'
    )

register('cmsbootstrap.ie8_js', ie8_js)

ie8_css = Bundle(
    'cmsbootstrap/ie8.css',
    filters='cssmin',
    output='css/cmsbootstrap/ie8.min.css',
    depends='sass/*.scss')

register('cmsbootstrap.ie8_css', ie8_css)

ie7_js = Bundle(
    'cmsbootstrap/ie7.js',
    filters='jsmin',
    output='js/cmsbootstrap/ie7.min.js'
    )

register('cmsbootstrap.ie7_js', ie7_js)

ie7_css = Bundle(
    'cmsbootstrap/ie7.css',
    filters='cssmin',
    output='css/cmsbootstrap/ie7.min.css',
    )

register('cmsbootstrap.ie7_css', ie7_css)
