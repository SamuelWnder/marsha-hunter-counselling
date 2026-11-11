<?php
/**
 * Marsha Hunter Counselling — single landing page theme.
 */

add_action( 'after_setup_theme', function () {
	add_theme_support( 'title-tag' );
} );

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style(
		'marsha-hunter-fonts',
		'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'marsha-hunter', get_stylesheet_uri(), array(), '1.0' );
} );

add_action( 'wp_head', function () {
	$title       = 'Marsha Hunter Counselling';
	$description = 'BACP-registered counsellor offering online counselling for individuals and couples via Zoom.';
	?>
	<link rel="icon" type="image/svg+xml" href="<?php echo esc_url( get_theme_file_uri( 'images/favicon.svg' ) ); ?>">
	<link rel="icon" type="image/png" sizes="192x192" href="<?php echo esc_url( get_theme_file_uri( 'images/favicon-192.png' ) ); ?>">
	<link rel="apple-touch-icon" href="<?php echo esc_url( get_theme_file_uri( 'images/apple-touch-icon.png' ) ); ?>">
	<meta property="og:type" content="website">
	<meta property="og:locale" content="en_GB">
	<meta property="og:url" content="<?php echo esc_url( home_url( '/' ) ); ?>">
	<meta property="og:title" content="<?php echo esc_attr( $title ); ?>">
	<meta property="og:description" content="<?php echo esc_attr( $description ); ?>">
	<meta property="og:image" content="<?php echo esc_url( get_theme_file_uri( 'images/share.jpg' ) ); ?>">
	<meta property="og:image:width" content="1200">
	<meta property="og:image:height" content="630">
	<meta name="twitter:card" content="summary_large_image">
	<?php
} );
