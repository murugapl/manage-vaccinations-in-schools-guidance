from process_images import process_consent_matching, process_get_consent, process_get_gillick_competent_consent, process_pre_screening, process_sessions_add_dates


IMAGES = [
    {
        "description": "Screenshot of a potential match for an unmatched consent response.",
        "image_name": "consent-link.png",
        "url_extension": "consent-forms/1",
        "screen_size": {    
            "width": 700,
            "height": 1080
        },
        "further_processing": process_consent_matching
    },
    {
        "description": "Screenshot of selecting paper as the response method.",
        "image_name": "consent-response-paper.png",
        "url_extension": "sessions/1/consents/given",
        "screen_size": {    
            "width": 700,
            "height": 1080
        },
        "further_processing": process_get_consent
    },
    {
        "description": "Screenshot of a list of unmatched consent responses.",      
        "image_name": "consent-unmatched.png",
        "url_extension": "consent-forms",
        "screen_size": {    
            "width": 1500,
            "height": 1080
        },
        "full_page": True
    },
    # {
    #     "description": "Screenshot of important notices page.",       #ask about how to create notices
    #     "image_name": "notices.png",
    #     "url_extension": "notices",
    #     "screen_size": {    
    #         "width": 1500,
    #         "height": 1080
    #     },
    #     "login": {
    #         "username": "superuser@example.com",
    #         "password": "superuser@example.com"
    #     },
    #     "full_page": True
    # },
    # {
    #     "description": "Screenshot of important notices page.",       #screenshotting excel?
    #     "image_name": "offline-spreadsheet.png",
    #     "screen_size": {    
    #         "width": 1500,
    #         "height": 1080
    #     },
    # },
    {
        "description": "Screenshot of the offline recording spreadsheet.",       #not used anywhere in the guide
        "image_name": "organisation.png",
        "url_extension": "organisation",
        "screen_size": {    
            "width": 1150,
            "height": 1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of programme cohorts tab.",       
        "image_name": "programme-cohorts.png",
        "url_extension": "programmes/hpv/cohorts",
        "screen_size": {    
            "width": 1300,
            "height": 100
        },
        "full_page": True
    },
    {
        "description": "Screenshot of the programme overview page.",     
        "image_name": "programme-overview.png",
        "url_extension": "programmes/hpv",
        "screen_size": {    
            "width": 1200,
            "height": 900
        },
        "full_page": True
    },
    {
        "description": "Screenshot of cohort triage.",     
        "image_name": "programme-triage.png",
        "url_extension": "programmes/hpv/patients",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
    },
    {
        "description": "Screenshot of programme vaccinations tab.",     
        "image_name": "programme-vaccinations.png",
        "url_extension": "programmes/hpv/vaccination-records",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
    },
    {
        "description": "Screenshot of page showing children who have moved school.",     
        "image_name": "school-move-list.png",
        "url_extension": "school-moves",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
    },
    {
        "description": "Screenshot of page showing children who have moved school.",     
        "image_name": "school-move-review.png",
        "url_extension": "school-moves/1",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of a register attendance page.",
        "image_name": "session-attendance.png",
        "url_extension": "sessions/1/attendances/unregistered?sort=name&direction=asc",
        "screen_size": {    
            "width": 1100,
            "height": 1080
        }
    },
    {
        "description": "Screenshot of pre-screening questions on a patient record.",     
        "image_name": "session-child-pre-screen.png",
        "url_extension": "sessions/1/vaccinations/vaccinate",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "further_processing": process_pre_screening
    },
    {
        "description": "Screenshot of overview page for a completed session.",     
        "image_name": "session-completed.png",
        "url_extension": "sessions/2",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of selecting a Gillick competent child.",     
        "image_name": "session-consent-gillick-competent.png",
        "url_extension": "sessions/1/consents/given",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "further_processing": process_get_gillick_competent_consent
    },
    {
        "description": "Screenshot of consent responses for a session.",     
        "image_name": "session-consent.png",
        "url_extension": "sessions/1/consents/no-consent",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of session edit screen with session dates added.",     
        "image_name": "session-edit-with-dates.png",
        "url_extension": "sessions/1/edit",
        "screen_size": {    
            "width": 1300,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of session edit screen without any session dates added.",     
        "image_name": "session-edit-without-dates.png",
        "url_extension": "sessions/unscheduled",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "further_processing": process_sessions_add_dates
    },
    {
        "description": "Screenshot of the check consent responses page.",     
        "image_name": "session-no-consent-response.png",
        "url_extension": "sessions/1/consents/no-consent",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of a session overview page.",     
        "image_name": "session.png",
        "url_extension": "sessions/1",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "description": "Screenshot of vaccines page.",     
        "image_name": "vaccines.png",
        "url_extension": "vaccines",
        "screen_size": {    
            "width": 1200,
            "height":1080
        },
    },
]

