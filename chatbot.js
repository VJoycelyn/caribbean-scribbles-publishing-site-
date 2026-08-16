/*
 * Caribbean Scribbles Publishing — Island Guide
 *
 * This is intentionally client-side and does not collect or store chat messages.
 * It uses a small, curated knowledge base so the GitHub Pages site never exposes
 * an API key. Questions needing a quote, manuscript review, rights guidance, or
 * a bespoke publishing decision are routed to the existing contact form/email.
 */
(function () {
  "use strict";

  var launcher = document.getElementById("chatbot-launcher");
  var panel = document.getElementById("chatbot-panel");
  var closeButton = document.getElementById("chatbot-close");
  var messages = document.getElementById("chatbot-messages");
  var suggestions = document.getElementById("chatbot-suggestions");
  var form = document.getElementById("chatbot-form");
  var input = document.getElementById("chatbot-input");

  if (!launcher || !panel || !closeButton || !messages || !suggestions || !form || !input) return;

  var links = {
    services: { label: "See services", href: "#services" },
    authors: { label: "For authors", href: "#authors" },
    books: { label: "Browse books", href: "#shop" },
    contact: { label: "Contact form", href: "#contact" },
    newsletter: { label: "Weekly newsletter", href: "#newsletter" },
    email: { label: "Email Caribbean Scribbles", href: "mailto:caribbeanscribbles@gmail.com" },
    whatsapp: { label: "Message on WhatsApp", href: "https://wa.me/18696639220" }
  };

  var books = [
    {
      name: "My Kindergarten Handbook: Little Kinder Kids",
      age: "Ages 4–6",
      topic: "school readiness, handwriting, numbers, and confidence",
      href: "https://www.amazon.com/My-Kindergarten-Handbook-Little-Kinder/dp/B0F4M2QL24",
      keywords: ["kindergarten", "school readiness", "early learner", "handwriting", "counting"]
    },
    {
      name: "Island Lab: 15 Caribbean Science Experiments",
      age: "Ages 6–12",
      topic: "hands-on Caribbean STEM and science activities",
      href: "https://www.amazon.com/Island-Lab-Caribbean-Experiments-Explorers/dp/B0GY155LQ2",
      keywords: ["island lab", "stem", "science", "experiment", "experiments"]
    },
    {
      name: "Akejah and the Rules of Harmony Island",
      age: "Ages 6–10",
      topic: "kindness, courage, community, and values",
      href: "https://www.amazon.com/Akejah-Rules-Harmony-island-Caribbean/dp/B0G3F2GTFM",
      keywords: ["akejah", "harmony", "values", "kindness", "courage", "community"]
    },
    {
      name: "Sweets, Treats, Toys & Me!",
      age: "Ages 5–10",
      topic: "childhood, island spirit, and early entrepreneurship",
      href: "https://www.amazon.com/Sweets-Treats-Toys-Entrepreneurial-Adventure/dp/B0GXRNHRHS",
      keywords: ["sweets", "treats", "toys", "entrepreneur", "entrepreneurship", "business"]
    },
    {
      name: "The Jingle of the Sugar Mas Bells",
      age: "Ages 5–10",
      topic: "Saint Kitts Christmas, carnival colour, and Sugar Mas",
      href: "https://www.amazon.com/Jingle-Sugar-Mas-Bells/dp/B0G473HPSN",
      keywords: ["jingle", "sugar mas", "christmas", "holiday", "carnival"]
    },
    {
      name: "Saint Kitts Pride: Exercise Book",
      age: "All ages",
      topic: "writing practice and Saint Kitts & Nevis pride",
      href: "https://www.amazon.com/Saint-Kitts-Pride-Exercise-Book/dp/B0FL15G3KL",
      keywords: ["saint kitts pride", "exercise book", "writing practice", "island pride"]
    },
    {
      name: "The Girls of My Sketchbook: Hairstyles, Habitats & Hobbies",
      age: "All ages",
      topic: "creative colouring, representation, and natural hairstyles",
      href: "https://www.amazon.com/Girls-My-Sketchbook-Hairstyles-Habitats/dp/B0H1HM6D8G",
      keywords: ["girls", "sketchbook", "coloring", "colouring", "drawing", "hairstyles", "hobbies"]
    }
  ];

  var quickQuestions = [
    "What publishing services do you offer?",
    "Which book is best for ages 4–6?",
    "How can I order a book?",
    "How do I request publishing assistance?"
  ];

  function normalize(value) {
    return String(value || "")
      .toLowerCase()
      .replace(/[–—]/g, "-")
      .replace(/[^a-z0-9\s&-]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function addMessage(role, text, messageLinks) {
    var wrapper = document.createElement("div");
    wrapper.className = "chatbot-message " + role;
    wrapper.textContent = text;

    if (messageLinks && messageLinks.length) {
      var linkRow = document.createElement("div");
      linkRow.className = "chatbot-links";
      messageLinks.forEach(function (link) {
        var anchor = document.createElement("a");
        anchor.className = "chatbot-link";
        anchor.href = link.href;
        anchor.textContent = link.label;
        if (/^https?:\/\//i.test(link.href)) {
          anchor.target = "_blank";
          anchor.rel = "noopener";
        }
        linkRow.appendChild(anchor);
      });
      wrapper.appendChild(linkRow);
    }

    messages.appendChild(wrapper);
    messages.scrollTop = messages.scrollHeight;
  }

  function renderSuggestions() {
    suggestions.innerHTML = "";
    quickQuestions.forEach(function (question) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "chatbot-suggestion";
      button.textContent = question;
      button.addEventListener("click", function () {
        askQuestion(question);
      });
      suggestions.appendChild(button);
    });
  }

  function bookLinks(book) {
    return [
      { label: "View on Amazon", href: book.href },
      links.books
    ];
  }

  function findBook(question) {
    for (var i = 0; i < books.length; i += 1) {
      var book = books[i];
      if (book.keywords.some(function (keyword) { return question.indexOf(keyword) !== -1; })) return book;
    }
    return null;
  }

  function answer(question) {
    var q = normalize(question);
    var book = findBook(q);

    if (!q) {
      return { text: "Tell me what you need help with—books, ordering, publishing services, workshops, or contacting the team.", links: [links.services, links.books, links.contact] };
    }

    if (/^(hi|hello|hey|good morning|good afternoon|good evening)\b/.test(q)) {
      return { text: "Welcome to Caribbean Scribbles Publishing. I can help you explore our books, understand publishing support, or find the best next step for your project.", links: [links.books, links.services, links.contact] };
    }

    if (/(price|cost|rate|quote|how much|timeline|turnaround|how long)/.test(q) && /(publish|publishing|manuscript|editing|book|project|workshop|service)/.test(q)) {
      return { text: "Publishing support is tailored to the project, so the best next step is to share your idea, audience, current draft stage, and the help you need. The team can then discuss fit, scope, timing, and pricing directly.", links: [links.contact, links.email] };
    }

    if (/(manuscript|draft|story idea|story coaching|writing help|feedback|structure|character|setting|voice)/.test(q)) {
      return { text: "Caribbean Scribbles offers practical manuscript and story coaching, including story idea and structure review, character and setting development, and feedback focused on clarity and voice. Use the contact form to describe your readers and where you are in the writing process.", links: [links.authors, links.contact] };
    }

    if (/(edit|editing|copyedit|line edit|layout|typeset|interior|design|print ready|file preparation|kdp|ingramspark|isbn|self publish|self-publish|production)/.test(q)) {
      return { text: "The publishing team can help with light copyediting and line checks, typesetting and interior design, print-ready file preparation, and setup guidance for platforms such as Amazon KDP or IngramSpark. Specific requirements and pricing are discussed after reviewing your project.", links: [links.services, links.contact] };
    }

    if (/(school|schools|ngo|nonprofit|church|group|classroom|workshop|author talk|creative session|bulk order|community event)/.test(q)) {
      return { text: "Schools, NGOs, churches, and community groups can ask about custom workbooks, activity books, author talks, creative writing sessions, and small-batch printing guidance. Send the group size, audience, location, and preferred timing through the contact form.", links: [links.services, links.contact] };
    }

    if (/(what services|which services|services do you offer|publishing services)/.test(q)) {
      return { text: "Caribbean Scribbles offers three main types of support: manuscript and story coaching; editing, layout, and publishing setup for platforms such as KDP or IngramSpark; and custom projects or workshops for schools, NGOs, churches, and community groups.", links: [links.services, links.contact] };
    }

    if (/(publish with us|publishing help|publishing assistance|publishing service|publishing support|become an author|how do i publish|how can i publish|publish my book|publishing process|book project)/.test(q)) {
      return { text: "The usual path is: share your idea, review the story and structure, prepare the design and publishing files, then plan launch support. Caribbean Scribbles works with children’s books, middle grade and chapter books, workbooks, school resources, and digital-first Caribbean storytelling.", links: [links.authors, links.services, links.contact] };
    }

    if (/(order|buy|purchase|where can i get|where do i get|shipping|amazon|whatsapp)/.test(q)) {
      return { text: "You can browse the book shelf, purchase through the linked Amazon pages, or message Caribbean Scribbles on WhatsApp about an order. For bulk, school, or local-order questions, use the contact form.", links: [links.books, links.whatsapp, links.contact] };
    }

    if (book) {
      return { text: book.name + " is for " + book.age + " and focuses on " + book.topic + ".", links: bookLinks(book) };
    }

    if (/(ages? 4|4-6|preschool|early learner|kindergarten)/.test(q)) {
      return { text: "For ages 4–6, start with My Kindergarten Handbook: Little Kinder Kids. It supports school readiness, handwriting, numbers, and confidence-building.", links: bookLinks(books[0]) };
    }

    if (/(ages? 6|6-12|stem|science|experiment)/.test(q)) {
      return { text: "For ages 6–12, Island Lab is a strong choice for hands-on Caribbean STEM and science activities.", links: bookLinks(books[1]) };
    }

    if (/(recommend|suggest|best book|which book|book for|children|child|reader)/.test(q)) {
      return { text: "I can help narrow it down by age or interest. For ages 4–6, try My Kindergarten Handbook; for ages 6–12, try Island Lab; for values and community, try Akejah and the Rules of Harmony Island. You can also browse the full shelf.", links: [bookLinks(books[0])[0], bookLinks(books[1])[0], bookLinks(books[2])[0], links.books] };
    }

    if (/(newsletter|subscribe|weekly picks|email updates)/.test(q)) {
      return { text: "You can join the weekly recommendations list on this page, or visit the Newsletter Hub for the rotating book picks and updates.", links: [links.newsletter, { label: "Newsletter Hub", href: "https://caribbooks-kcnjhnv4.manus.space" }] };
    }

    if (/(contact|email|reach|message|phone|instagram|social|whatsapp)/.test(q)) {
      return { text: "Caribbean Scribbles Publishing is based in Saint Kitts & Nevis. For publishing requests, book questions, workshops, or general enquiries, email caribbeanscribbles@gmail.com or use the contact form.", links: [links.contact, links.email, links.whatsapp] };
    }

    if (/(where are you|location|based|saint kitts|nevis|caribbean)/.test(q)) {
      return { text: "Caribbean Scribbles Publishing is based in Saint Kitts & Nevis and supports Caribbean-rooted stories, authors, schools, NGOs, and creative projects.", links: [links.about || { label: "About us", href: "#about" }, links.contact] };
    }

    if (/(copyright|rights|royalt|legal|contract|representation|submission|submit|unsolicited)/.test(q)) {
      return { text: "Rights, representation, contracts, and submission decisions need a direct conversation rather than an automated answer. Please share the relevant context through the contact form or email the team.", links: [links.contact, links.email] };
    }

    return { text: "I can help with book recommendations, ordering, publishing services, manuscript coaching, editing and layout, KDP/IngramSpark setup, school or NGO projects, workshops, newsletters, and contact details. For anything project-specific, please use the contact form.", links: [links.services, links.books, links.contact] };
  }

  function askQuestion(question) {
    var cleanQuestion = String(question || "").trim();
    if (!cleanQuestion) return;
    addMessage("user", cleanQuestion);
    input.value = "";
    var response = answer(cleanQuestion);
    window.setTimeout(function () {
      addMessage("bot", response.text, response.links);
    }, 180);
  }

  function setOpen(open) {
    panel.classList.toggle("open", open);
    panel.setAttribute("aria-hidden", String(!open));
    launcher.setAttribute("aria-expanded", String(open));
    if (open) {
      input.focus();
    }
  }

  launcher.addEventListener("click", function () {
    setOpen(!panel.classList.contains("open"));
  });

  closeButton.addEventListener("click", function () {
    setOpen(false);
    launcher.focus();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && panel.classList.contains("open")) {
      setOpen(false);
      launcher.focus();
    }
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    askQuestion(input.value);
  });

  renderSuggestions();
  addMessage("bot", "Hi! I’m Island Guide. Ask me about publishing assistance, book recommendations, ordering, workshops, or the best next step for your project.", [links.services, links.books, links.contact]);
})();
