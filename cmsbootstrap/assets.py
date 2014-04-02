from django_assets import Bundle, register

bootstrap_css = Bundle(
    'sass/bootstrap/bootstrap.scss',
    filters='pyscss, cssmin',
    output='css/bootstrap.css',
    depends='sass/bootstrap/*.scss')

register('bootstrap_css', bootstrap_css)

cmsbootstrap_css = Bundle(
    'sass/cmsbootstrap.scss',
    filters='pyscss, cssmin',
    output='css/cmsbootstrap.css',
    depends='sass/*.scss')

register('cmsbootstrap_css', cmsbootstrap_css)
