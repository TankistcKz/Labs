package org.example.controller;

import org.example.service.*;
import org.springframework.context.ApplicationContext;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NotificationController {
    private final NotificationManager notificationManager;

    public NotificationController(NotificationManager notificationManager) {
        this.notificationManager = notificationManager;
    }

    @GetMapping("/notify")
    public String notify(@RequestParam String message, @RequestParam String email) {
        notificationManager.notify(message, email);
        return "Уведомление отправлено (аннотации)";
    }
    
// 	private final ApplicationContext context;
// 	
// 	public NotificationController(ApplicationContext context) {
// 	    this.context = context;
// 	}
// 	
// 	@GetMapping("/notify")
// 	public String notify(@RequestParam String message, @RequestParam String email) {
// 	    NotificationManager manager = context.getBean(NotificationManager.class);
// 	    manager.notify(message, email);
// 	    return "Уведомление отправлено через Java Config";
// 	}
// }

//     @GetMapping("/notify")
//     public String notify(
//             @RequestParam String message, 
//             @RequestParam String email,
//             @RequestParam(defaultValue = "email") String type) {
//         
//         MessageService service;
//         
//         switch (type.toLowerCase()) {
//             case "sms":
//                 service = new SmsService();
//                 break;
//             case "push":
//                 service = new PushService();
//                 break;
//             case "email":
//             default:
//                 service = new EmailService();
//                 break;
//         }
//         
//         NotificationManager manager = new NotificationManager(service);
//         manager.notify(message, email);
//         
//         return "Уведомление отправлено через " + type;
//     }
}
