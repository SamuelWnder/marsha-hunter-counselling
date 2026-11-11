<?php
/**
 * Single landing page.
 *
 * CONTACT DETAILS: change the two values below — they are used everywhere on the page.
 */
$mh_email = 'email@example.com';
$mh_phone = '07000 000000';
?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Marsha Hunter is a BACP-registered counsellor offering online counselling for individuals and couples via Zoom.">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="#top" id="top">
      <svg class="brand-mark" viewBox="0 0 48 32" aria-hidden="true" focusable="false">
        <g stroke="#ecc45a" stroke-width="2.6" stroke-linecap="round">
          <path d="M24 10 V5"/>
          <path d="M32 12.1 L34.5 7.8"/>
          <path d="M16 12.1 L13.5 7.8"/>
          <path d="M37.9 18 L42.2 15.5"/>
          <path d="M10.1 18 L5.8 15.5"/>
        </g>
        <path d="M12 27 A12 12 0 0 1 36 27 Z" fill="#ecc45a"/>
        <path d="M3 28 H45" stroke="#35543f" stroke-width="2.6" stroke-linecap="round"/>
      </svg>
      <span class="brand-text">Marsha Hunter <span>Counselling</span></span>
    </a>
    <nav class="nav" aria-label="Main">
      <a href="#about">About</a>
      <a href="#approach">Approach</a>
      <a href="#fees">Fees</a>
      <a class="btn btn-primary nav-cta" href="#contact">Get in touch</a>
    </nav>
  </div>
</header>

<main id="main">

  <section class="hero">
    <div class="wrap">
      <div>
        <h1>A safe space to feel <em>heard</em>.</h1>
        <p class="hero-lead">I'm Marsha Hunter, a qualified and experienced counsellor. I offer a welcoming, non-judgemental space where you can work through challenging feelings and situations.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#contact">Arrange an initial session</a>
          <a class="btn btn-ghost" href="#fees">Session fees</a>
        </div>
        <ul class="hero-facts">
          <li>Registered with the BACP</li>
          <li>Individuals and couples</li>
          <li>Sessions via Zoom</li>
        </ul>
      </div>

      <div class="hero-art">
        <img src="<?php echo esc_url( get_theme_file_uri( 'images/marsha-hunter.jpg' ) ); ?>" alt="Marsha Hunter, counsellor" width="1254" height="1254">
      </div>
    </div>
    <svg class="hero-curve" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 0 Q 50 200 100 0 V100 H0 Z" fill="#ffffff"/></svg>
  </section>

  <section class="section section-white about" id="about">
    <div class="wrap">
      <div>
        <span class="eyebrow">About me</span>
        <h2>Qualified, experienced and here to listen.</h2>
        <ul class="credentials">
          <li>Registered with the BACP</li>
          <li>Level 5 Diploma in Psychotherapeutic Counselling <small>Headstrong Academy</small></li>
          <li>Diploma in Therapeutic Counselling <small>Headstrong Academy</small></li>
          <li>Intensive training in Couples Counselling</li>
        </ul>
      </div>
      <div class="about-body">
        <p>I'm Marsha Hunter, a qualified and experienced counsellor, registered with the BACP, with a passion for creating a safe space for both individuals and couples.</p>
        <p>I obtained my Diploma in Therapeutic Counselling, followed by an advanced Level 5 Diploma in Psychotherapeutic Counselling at Headstrong Academy. I have also undertaken intensive training in Couples Counselling, deepening my understanding of the complexities of relationships, affairs and betrayal, separation, the processes of rebuilding trust, repairing relationships and strengthening communication, and GSRD (gender, sexuality and relationship diversity) relationships.</p>
        <p>I create a welcoming and non-judgemental space where individuals and couples can feel heard and work through challenging feelings and situations.</p>
      </div>
    </div>
  </section>

  <section class="section section-green" id="approach">
    <div class="wrap">
      <div class="approach-head">
        <span class="eyebrow">My approach</span>
        <h2>Relational and kind.</h2>
        <p>You can bring the issues that feel relevant and important to you. Whether you're navigating relationship difficulties, facing personal challenges or just wanting to understand yourself better, my door is open to you.</p>
      </div>

      <div class="approach-grid">
        <article class="card">
          <h3>Individual counselling</h3>
          <p>A space that is yours, to explore what you're facing at your own pace and to understand yourself better.</p>
          <ul class="tags">
            <li>Personal challenges</li>
            <li>Relationship difficulties</li>
            <li>Understanding yourself</li>
          </ul>
        </article>
        <article class="card">
          <h3>Couples counselling</h3>
          <p>Support for both of you to feel heard, to work through what has happened and to find a way forward.</p>
          <ul class="tags">
            <li>Affairs and betrayal</li>
            <li>Rebuilding trust</li>
            <li>Strengthening communication</li>
            <li>Repairing relationships</li>
            <li>Separation</li>
            <li>Gender, sexuality and relationship diversity</li>
          </ul>
        </article>
      </div>

      <blockquote class="pull">
        I don't believe therapy should be a space where you talk to someone who simply sits back and listens. I believe that, as a therapist, it is my job to explore your experiences together, with curiosity, openness and without judgement.
      </blockquote>
    </div>
  </section>

  <section class="section section-white" id="fees">
    <div class="wrap">
      <div class="fees-head">
        <div>
          <span class="eyebrow">Session fees</span>
          <h2>Simple, clear pricing.</h2>
        </div>
        <p class="zoom-note">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#35543f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="14" height="12" rx="3"/><path d="m16 10 6-3v10l-6-3"/></svg>
          I currently offer sessions via Zoom
        </p>
      </div>

      <div class="fees-grid">
        <div class="fee">
          <h3>Individual counselling</h3>
          <p class="fee-price"><strong>£55</strong> per session</p>
          <p class="fee-block"><strong>£50 per session</strong> when booking a block of four.</p>
        </div>
        <div class="fee">
          <h3>Couples counselling</h3>
          <p class="fee-price"><strong>£75</strong> per session</p>
          <p class="fee-block"><strong>£70 per session</strong> when booking a block of four.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section contact" id="contact">
    <svg class="contact-curve" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 100 Q 50 -100 100 100 Z" fill="#24392f"/></svg>
    <div class="wrap">
      <span class="eyebrow">Get in touch</span>
      <h2>Ready to take the next step?</h2>
      <p class="contact-lead">If you feel ready, please get in touch to arrange an initial session. I look forward to hearing from you.</p>
      <div class="contact-links">
        <a class="contact-link" href="mailto:<?php echo esc_attr( antispambot( $mh_email ) ); ?>">
          <small>Email</small>
          <span><?php echo esc_html( antispambot( $mh_email ) ); ?></span>
        </a>
        <a class="contact-link" href="tel:<?php echo esc_attr( preg_replace( '/[^0-9+]/', '', $mh_phone ) ); ?>">
          <small>Phone</small>
          <span><?php echo esc_html( $mh_phone ); ?></span>
        </a>
      </div>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap">
    <p class="crisis">This is not an emergency service. If you need urgent help, call Samaritans free on 116 123, or 999 in an emergency.</p>
    <p>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> Marsha Hunter Counselling</p>
    <p>Registered with the BACP &middot; Online sessions via Zoom</p>
  </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
