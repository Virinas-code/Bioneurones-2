#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bioneurones GUI.

A module for manipulating GUI for Bioneurones.
Use pygame.
"""
import sys
from typing import Any, Callable

import pygame
import pygame.display
import pygame.event
import pygame.image


class Ressource:
    def __init__(self, path) -> None:
        self.path = path
        self.image = pygame.image.load(self.path).convert()


class GUI:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((1200, 600))
        self.events: dict[int, function] = {}
    
    def add_event(self, key: int, function: Callable[[], Any]) -> None:
        self.events[key] = function
    
    def tick(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.display.flip()
