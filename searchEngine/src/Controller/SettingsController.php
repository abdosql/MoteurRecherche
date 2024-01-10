<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SettingsController extends AbstractController
{
    #[Route('/settings', name: 'app_settings')]
    public function index(): Response
    {
        $settings  = $this->readSettings("../settings/settings.json");
        return $this->render('settings/index.html.twig', [
            "settings" => $settings
        ]);
    }

    public function updatePath()
    {
        
    }
    public function readSettings($filePath): array
    {
        if (!file_exists($filePath)) {
            throw $this->createNotFoundException('The file does not exist.');
        }
        $jsonContents = file_get_contents($filePath);
        $jsonData = json_decode($jsonContents, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new \RuntimeException('Error decoding JSON: ' . json_last_error_msg());
        }
        return $jsonData;
    }
}
