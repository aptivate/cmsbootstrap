from django_assets import Bundle, register

bootstrap_css = Bundle(
    'sass/bootstrap/bootstrap.scss',
    filters='pyscss, cssmin',
    output='css/bootstrap.css',
    depends='sass/bootstrap/*.scss')

register('cmsbootstrap.bootstrap_css', bootstrap_css)

common_css = Bundle(
    'sass/cmsbootstrap.scss',
    filters='pyscss, cssmin',
    output='css/cmsbootstrap/common.css',
    depends='sass/*.scss')

register('cmsbootstrap.common_css', common_css)

ie8_css = Bundle(
    'css/cmsbootstrap/ie8.css',
    filters='cssmin',
    output='css/cmsbootstrap/ie8.min.css',
    depends='sass/*.scss')

register('cmsbootstrap.ie8_css', ie8_css)

common_js = Bundle(
    # don't encourage people to use this loader
    # 'js/cmsbootstrap/script_loader.js',
    'js/cmsbootstrap/ie_version.js',
    filters='jsmin',
    output='js/cmsbootstrap/common.js'
    )

register('cmsbootstrap.common_js', common_js)

ie8_js = Bundle(
    'js/html5shiv.js',
    'js/respond.min.js',
    filters='jsmin',
    output='js/cmsbootstrap/ie8.js'
    )

register('cmsbootstrap.ie8_js', ie8_js)
