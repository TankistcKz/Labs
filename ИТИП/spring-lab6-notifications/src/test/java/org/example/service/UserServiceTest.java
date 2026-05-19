package org.example.service;

import org.example.model.dto.UserDto;
import org.example.model.entity.User;
import org.example.repository.UserRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    void shouldCreateUser() {
        UserDto dto = new UserDto();
        dto.setName("Иван Иванов");
        dto.setEmail("ivan@example.com");
        dto.setPhone("+7-999-123-4567");

        User savedUser = new User();
        savedUser.setId(1L);
        savedUser.setName(dto.getName());
        savedUser.setEmail(dto.getEmail());
        savedUser.setPhone(dto.getPhone());

        when(userRepository.save(any(User.class))).thenReturn(savedUser);

        User result = userService.createUser(dto);

        assertNotNull(result);
        assertEquals("Иван Иванов", result.getName());
        assertEquals("ivan@example.com", result.getEmail());
        
        verify(userRepository, times(1)).save(any(User.class));
    }
    
    @Test
    void shouldCallSaveOnRepository() {
        UserDto dto = new UserDto();
        dto.setName("Иван");
        dto.setEmail("ivan@example.com");
    
        when(userRepository.save(any(User.class))).thenReturn(new User());
    
        userService.createUser(dto);
    
        verify(userRepository).save(any(User.class));
    }
    
    @Test
    void shouldGetUserById() {
        User user = new User();
        user.setId(1L);
        user.setName("Иван");
        user.setEmail("ivan@example.com");
    
        when(userRepository.findById(1L)).thenReturn(java.util.Optional.of(user));
    
        User result = userService.getUserById(1L);
    
        assertNotNull(result);
        assertEquals(1L, result.getId());
        assertEquals("Иван", result.getName());
        verify(userRepository).findById(1L);
    }
    
    @Test
    void shouldDeleteUser() {
        User user = new User();
        user.setId(1L);
        
        when(userRepository.findById(1L)).thenReturn(java.util.Optional.of(user));
        doNothing().when(userRepository).delete(user);
    
        userService.deleteUser(1L);
    
        verify(userRepository, times(1)).delete(user);
    }
}
