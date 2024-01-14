<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Finder\Finder;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SettingsController extends AbstractController
{
    #[Route('/settings', name: 'app_settings')]
    public function index(): Response
    {
        $settings  = $this->readSettings("../settings/settings.json");
        $path = $settings["path"];
        $files = $this->listFiles($path);
        return $this->render('settings/index.html.twig', [
            "settings" => $settings,
            "files" => $files
        ]);
    }
    #[Route("/settings/update", name: "updateSettings")]
    public function updatePath(Request $request): Response
    {

        $jsonData  = $this->readSettings("../settings/settings.json");
        $jsonData['path'] = $request->request->get("path");
        $jsonData['documents'] = $request->request->get("file");

        $updatedJsonContents = json_encode($jsonData, JSON_PRETTY_PRINT);

        file_put_contents("../settings/settings.json", $updatedJsonContents);

        return $this->redirectToRoute("app_settings");
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
    public function listFiles($directoryPath): array
    {
        $finder = new Finder();
        $finder->files()->in($directoryPath)->name('*.txt')->depth(0);

        $fileNames = [];

        foreach ($finder as $file) {
            $fileNames[] = $file->getBasename();
        }
        return $fileNames;
    }
}
