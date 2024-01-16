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
    #[Route('/results/{dataOutput}', name:'searchResults')]
    public function results($dataOutput): Response
    {
        return $this->render("home/results.html.twig", compact("dataOutput"));
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
        $pythonPath = "C:\ProgramData\anaconda3\python.exe";  // Adjust the path
        $pythonScriptPath = "C:\Users\seqqal\Documents\GitHub\Projects\MoteurRecherche\main.py";
        $process = new Process([
            $pythonPath, $pythonScriptPath, json_encode($data)
        ]);
        $process->run();
        if ($process->isSuccessful()){
            $dataOutput = $process->getOutput();

            return $this->redirectToRoute('searchResults', compact("dataOutput"));
        }
        $error = $process->getErrorOutput();
        return $this->render("error/index.html.twig", compact("error"));
    }
}
