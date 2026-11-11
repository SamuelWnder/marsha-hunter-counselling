import re
FONTS = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&display=swap"
s = open('theme/index.php').read()
s = s[s.index('<!doctype'):]
s = s.replace('<?php wp_head(); ?>', '<title>Marsha Hunter Counselling</title>\n<link rel="stylesheet" href="%s">\n<link rel="icon" href="theme/images/favicon.svg">\n<link rel="stylesheet" href="theme/style.css">' % FONTS)
s = s.replace("<?php echo esc_attr( antispambot( $mh_email ) ); ?>", "email@example.com").replace("<?php echo esc_html( antispambot( $mh_email ) ); ?>", "email@example.com")
s = s.replace("<?php echo esc_attr( preg_replace( '/[^0-9+]/', '', $mh_phone ) ); ?>", "07000000000").replace("<?php echo esc_html( $mh_phone ); ?>", "07000 000000")
s = s.replace("<?php echo esc_html( gmdate( 'Y' ) ); ?>", "2026").replace("<?php language_attributes(); ?>", 'lang="en-GB"').replace("<?php bloginfo( 'charset' ); ?>", "utf-8")
s = s.replace("<?php echo esc_url( get_theme_file_uri( 'images/marsha-hunter.jpg' ) ); ?>", "theme/images/marsha-hunter.jpg")
s = re.sub(r'\s*<\?php.*?\?>', '', s)
open('preview.html', 'w').write(s)
# index.html is the copy GitHub Pages serves; keep the work-in-progress out of search engines.
open('index.html', 'w').write(s.replace('<title>', '<meta name="robots" content="noindex">\n<title>', 1))
