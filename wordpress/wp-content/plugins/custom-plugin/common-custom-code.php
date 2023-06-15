<?php
/**
 * Plugin Name: Custom Plugin
 * Description: Provides custom code for common Wordpress specifications
 * Author: Jane Doe
 * Version: 1.0.0
 * Requires at least: 5.0
 * Requires PHP: 7.x
 * Tested up to: 6.x
 */

add_action( 'init', function() {
    register_block_type( dirname( __FILE__ ) . '/team' );
} );

// TODO: Add action to query backend User API and return response
