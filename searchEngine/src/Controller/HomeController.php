<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Process\Process;
use Symfony\Component\Routing\Annotation\Route;

class HomeController extends AbstractController
{
    #[Route('/', name: 'app_home')]
    public function index(): Response
    {
        return $this->render("home/index.html.twig");
    }
    #[Route('/results/{processOutput}', name:'searchResults')]
    public function results($processOutput): Response
    {
        return $this->render("home/results.html.twig", compact("processOutput"));
    }
    #[Route('/search', name: "search")]
    public function search(Request $request, SettingsController $settingsController): Response
    {

        $word = $request->request->get("word");
        $settings = $settingsController->readSettings("../settings/settings.json");
        $data = [
            "word" => $word,
            "settings" => $settings
        ];
        $condaEnvName = 'test';
        $pythonPath = 'C:\Users\seqqal\Documents\GitHub\Projects\MoteurRecherche\venv\Scripts\python';  // Adjust the path
        $activateScript = "C:\Users\seqqal\Documents\GitHub\Projects\MoteurRecherche\venv\Scripts\activate";  // Adjust the path

        $process = new Process([
            'cmd.exe', '/C', 'activate', $condaEnvName, '&&', $pythonPath, '../../main.py', json_encode($data)
        ]);
        $process->run();
        if ($process->isSuccessful()){
            $processOutput = $process->getOutput();
            return $this->redirectToRoute('searchResults', compact("processOutput"));
        }
        $error = $process->getErrorOutput();
        return $this->render("error/index.html.twig", compact("error"));
    }
}
